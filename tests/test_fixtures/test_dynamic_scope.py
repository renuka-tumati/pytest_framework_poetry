import pytest

value = 1


def determine_scope(fixture_name, config):
    if value == 1:
        return "session"
    return "function"


""" cannot invoke a lower scope fixture from higher scope"""


@pytest.fixture(scope="session")
def num():
    return [1, 2, 3]


@pytest.fixture(scope=determine_scope)
def num_fixture(num):
    num.append(4)
    return num


@pytest.fixture(scope="function")
def num1():
    return [1, 2, 3]


@pytest.fixture(scope="session")
def val_fixture(num1):
    num.append(4)
    return num


def test_dynamic_scope_1(num_fixture):
    print(num_fixture)
    assert True


def test_dynamic_scope_2(num_fixture):
    print(num_fixture)
    assert True

