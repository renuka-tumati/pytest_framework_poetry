import pytest

from fixtures_yield import Email, MailAdminClient


@pytest.fixture
def mail_admin():
    return MailAdminClient()


@pytest.fixture
def sending_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)


@pytest.fixture
def receiving_user(mail_admin, request):
    user = mail_admin.create_user()

    def delete_user():
        mail_admin.delete_user(user)

    request.addfinalizer(delete_user)
    return user


@pytest.fixture
def email(sending_user, receiving_user, request):
    _email = Email(subject="Hey!", body="How's it going?")
    sending_user.send_email(_email, receiving_user)

    def empty_mailbox():
        receiving_user.clear_mailbox()

    request.addfinalizer(empty_mailbox)
    return _email


def test_email_received(receiving_user, email):
    assert email in receiving_user.inbox


@pytest.fixture(scope = "function")
def num(request):
    list_num = [1, 2, 3]

    def final_reset():
        print("reset 1")

    request.addfinalizer(final_reset)
    return list_num


"""Finalizers are executed in a first-in-last-out order. For yield fixtures, 
the first teardown code to run is from the right-most fixture, i.e. the last test parameter."""


@pytest.fixture
def num_finalizer(num, request):
    print("\n check 0")
    list_n = num.append(4)
    print("check 1")

    def reset_num():
        print("reset num")

    print("check 2")
    request.addfinalizer(reset_num)
    print("check 3")
    return list_n


def test_num_list(num_finalizer, num):
    print("check 4")
    print(num_finalizer)
    assert True
    print("check 5")


def test_bar(fix_w_yield1, fix_w_yield2):
    print("test_bar")


@pytest.fixture
def fix_w_yield1():
    yield
    print("after_yield_1")


@pytest.fixture
def fix_w_yield2():
    yield
    print("after_yield_2")