import pytest
import smtplib


@pytest.fixture(scope="function")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


@pytest.fixture
def initialize():
    return "Initialized"

"""As you can see, a fixture with the same name can be overridden for certain test folder level. Note that 
the base or super fixture can be accessed from the overriding fixture easily - used in the example below.
tests folder username fixture is invoked first"""
@pytest.fixture
def username(username):
    print("Test_fixtures conftest", username)
    return 'overridden-' + username

def test_username(username):
    print("Test_username", username)
    assert username == 'overridden-username'


@pytest.fixture
def other_username(username):
    return 'other-' + username

@pytest.fixture
def any_val(username):
    return 'other-' + username


@pytest.mark.parametrize('username', ['directly-overridden-username'])
def test_username(username):
    assert username == 'directly-overridden-username'


@pytest.mark.parametrize('username', ['directly-overridden-username-other'])
def test_username_other(any_val):
    assert any_val == 'other-directly-overridden-username-other'
