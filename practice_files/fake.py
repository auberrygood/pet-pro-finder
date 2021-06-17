from faker import Faker

fake = Faker('en_US')
Faker.seed(5567)

for _ in range(10):
    print(f" Name: {fake.name()}, \n Address: {fake.address()}")
    print()