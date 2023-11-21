from data.data import PersonData, fake


def generate_person_data():
    person = PersonData()
    person.name = fake.name()
    person.country = fake.country()
    person.city = fake.city()
    person.credit_card = fake.credit_card_number()
    person.month = fake.month()
    person.year = fake.year()
    person.password = fake.password()
    return person
