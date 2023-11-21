from faker import Faker

fake = Faker()


class PersonData:
    name: str = None
    country: str = None
    city: str = None
    credit_card: int = None
    month: int = None
    year: int = None
    password: str = None
