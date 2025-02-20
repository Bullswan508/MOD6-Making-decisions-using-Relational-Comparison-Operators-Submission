from faker import Faker
import numpy as np

fake = Faker()

random_phone_numbers = []
texts_from_phone_numbers = []

# Generate multiple phone numbers
for _ in range(100):
    random_phone_numbers.append(fake.msisdn()[3:])

mu = 250
sigma = 70

for phone_number in random_phone_numbers:
    texts_from_phone_numbers.extend([phone_number] * int(np.random.normal(mu, sigma)))

np.random.shuffle(texts_from_phone_numbers)

with open('./text_data', 'w') as file:
    for phone_number in texts_from_phone_numbers:
        file.write(f"Text sent from ({phone_number[:3]})-{phone_number[3:6]}-{phone_number[6:]}\n")
    file.close()