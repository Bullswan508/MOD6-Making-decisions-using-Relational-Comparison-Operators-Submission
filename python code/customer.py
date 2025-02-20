# Customer class
# Stores info about the customer's phone number, the amount of texts sent, bill info, etc.

from constants import *

class Customer():

    def __init__(self, number, num_texts):
        self.phone_number = number
        self.phone_number_str = f'({self.phone_number[:3]})-{self.phone_number[3:6]}-{self.phone_number[6:]}'
        self.num_texts = num_texts
        self.bill_amount = self.create_bill_statement(self.num_texts)

    def __str__(self):
        return(f'Customer phone number is {self.phone_number_str} and has sent {self.num_texts} texts.')

    def __repr__(self):
        return(f'Phone Number={self.phone_number}, Num Texts={self.num_texts}, Bill Amount={self.bill_amount}')

    def create_bill_statement(self, num_texts):

        if num_texts <= 100:
            return BASE_BILL_AMOUNT * BILL_TAX_MULTIPLIER
        
        if num_texts <= 300:
            return ((num_texts - 100) * 0.03 + BASE_BILL_AMOUNT) * BILL_TAX_MULTIPLIER
        
        return (((num_texts - 300) * 0.02) + (200 * 0.03) + BASE_BILL_AMOUNT) * BILL_TAX_MULTIPLIER
        

    