from faker import Faker

fake = Faker()

name = fake.name()
address = fake.address()
email = fake.email()    


print("Name:", name)
print("Address:", address)
print("Email:", email)  