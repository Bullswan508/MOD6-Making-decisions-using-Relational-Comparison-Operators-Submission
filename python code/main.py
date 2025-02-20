from collections import Counter
from customer import Customer

def get_text_data(file_path='./python code/text_data.txt'):

    phone_numbers = []
    
    with open(file_path, 'r') as file:

        for line in file:
            phone_number = ''.join(filter(str.isdigit, line))

            # Sentinel Test
            if phone_number == '0000000000':
                print('Data Import Finished')
                break

            phone_numbers.append(phone_number)

    return Counter(phone_numbers)

# Creates an array of customer objects
def create_customers(data):

    customers = []

    for phone_number, num_texts in data.items():
        customers.append(Customer(phone_number, num_texts))

    return customers

def display_customer_data(customer):
    print(f"Customer with phone number {customer.phone_number_str} sent {customer.num_texts} texts and has a bill of ${customer.bill_amount:.2f}")


def first_scenario(customers):
    """Displays all customer data"""

    print("Displaying all customer data collected:")
    print("---------------------------------------")

    for customer in customers:
        display_customer_data(customer)
    
    return None


def second_scenario(customers):
    """Displays data for customers who sent >100 texts"""

    print("Displaying all cumstomers who sent more than 100 texts:")
    print("-------------------------------------------------------")

    for customer in customers:
        if customer.num_texts > 100:
            display_customer_data(customer)

    return None

def third_scenario(customers):
    """Displays data for customers who have a bill >$10"""

    print("Displaying all customers who owe more than $10:")
    print("-----------------------------------------------")

    for customer in customers:
        if customer.bill_amount > 10:
            display_customer_data(customer)

    return None

def fourth_scenario(customers):
    """Displays customer data for a given area code"""

    area_code = input("What area code do you want to display customer data for?: ")

    title_str = f"Displaying all customers whose phone number has the area code {area_code}"

    print(title_str)
    print("-" * len(title_str))

    for customer in customers:
        if customer.phone_number[:3] == area_code:
            display_customer_data(customer)

    return None

def exit_scenario():

    print("Thank you for using this program!")

    return None

# -----------------
# --- Main Loop ---
# -----------------

if __name__ == "__main__":

    c = create_customers(get_text_data())

    user_option = None

    while True:
        
        print("")
        print("Please enter a number for the following options:")
        print("    - 1: Display All Customer Data")
        print("    - 2: Display All Data for Customers who sent more than 100 texts")
        print("    - 3: Display All Data for Customers who owe more than $10")
        print("    - 4: Display All Data for Texts Sent from Phone Numbers with a Selected Area Code")
        print("    - 5: Exit")
        print("")

        user_option = input("Which scenario are you choosing?: ")

        match user_option:

            case "1":
                first_scenario(c)

            case "2":
                second_scenario(c)

            case "3":
                third_scenario(c)

            case "4":
                fourth_scenario(c)

            case "5":
                exit_scenario()
                break

            case _:
                print("Error! That is not an option!")