"""_summary_

    Using faker library

"""

from faker import Faker

fake: Faker = Faker()

# get a random name
print(f"{fake.name() = }")
print(f"{fake.name() = }")
print(f"{fake.name() = }")
print(f"{fake.name() = }")

# get a random address
print(f"{fake.address() = }")
print(f"{fake.address() = }")
print(f"{fake.address() = }")
print(f"{fake.address() = }")

# get a random phone number
print(f"{fake.phone_number() = }")
print(f"{fake.phone_number() = }")
print(f"{fake.phone_number() = }")
print(f"{fake.phone_number() = }")