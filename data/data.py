from dataclasses import dataclass, field
from faker import Faker

fake = Faker()


@dataclass
class PersonData:
    name: str = field(default_factory=lambda: fake.name())
    country: str = field(default_factory=lambda: fake.country())
    city: str = field(default_factory=lambda: fake.city())
    credit_card: str = field(
        default_factory=lambda: fake.credit_card_number("visa")
    )
    month: str = field(default_factory=lambda: fake.month())
    year: str = field(default_factory=lambda: fake.year())
    password: str = field(default_factory=lambda: fake.password())
