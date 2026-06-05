import pytest


@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://www.saucedemo.com"
