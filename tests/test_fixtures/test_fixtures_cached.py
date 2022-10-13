import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order():
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    order.append(first_entry)
    """Return order.append(first_entry) - statement will not return changed order object only returns the none value"""
    return order


"""If a requested fixture was executed once for every time it was requested during a test,
 then this test would fail because both append_first and test_string_only would see order as an empty list (i.e. []), 
 but since the return value of order was cached (along with any side effects executing it may have had) after the 
 first time it was called, both the test and append_first were referencing the same object, and the test saw the 
 effect append_first had on that object."""


def test_string_only(append_first, order, first_entry):
    # Assert
    """ py.test tests/test_fixtures/test_fixtures_cached.py -s"""
    assert order == [first_entry]
    assert append_first == [first_entry]


def test_string(initialize):
    print("hello")
    assert "Initialized" == initialize
