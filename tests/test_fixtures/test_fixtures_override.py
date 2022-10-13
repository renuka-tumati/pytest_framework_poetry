import pytest

@pytest.fixture
def username():
    print("test file overload", username)
    return 'overridden-' + username

@pytest.fixture
def username(username):
    print("test file", username)
    return 'overridden-' + username


def test_username(username):
    print("Test_username", username)


