from dataclasses import dataclass


@dataclass(frozen=True)
class CheckoutInfo:
    first_name: str
    last_name: str
    postal_code: str


VALID_CUSTOMER = CheckoutInfo(first_name="Jan", last_name="Kowalski", postal_code="00-001")
