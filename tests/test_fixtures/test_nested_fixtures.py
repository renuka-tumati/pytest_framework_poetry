import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def second_entry():
    return 2


"""Fixture calling fixture and also multiple fixtures are being are used just like parameters"""


@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]


# Arrange
@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]


def test_string(order, expected_list):
    # Act
    order.append(3.0)

    # Assert
    assert order == expected_list


"""Fixtures can be requested more than once per test (return values are cached)
Fixtures can also be requested more than once during the same test, and pytest 
won’t execute them again for that test. This means we can request fixtures in multiple fixtures that are 
dependent on them (and even again in the test itself) without those fixtures being executed more than once."""

