from data.data import PersonData, fake


def generate_person_data() -> PersonData:
    """
    Generate a PersonData object with random values.

    Returns:
        PersonData: The generated person data.
    """
    # Create an instance of the PersonData class
    person = PersonData()

    # Generate random values for each attribute of the person object
    person.name = fake.name()
    person.country = fake.country()
    person.city = fake.city()
    person.credit_card = fake.credit_card_number()
    person.month = fake.month()
    person.year = fake.year()
    person.password = fake.password()

    # Return the generated person data
    return person
