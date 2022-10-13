import pytest


@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
    print(request.param)
    yield request.param
    print("finalizing {}".format(request.param))


@pytest.mark.parametrize("test_input", [1, 2])
def test_fixture_param(test_input, smtp_connection):
    print(smtp_connection)


""" Have to use request.param to read the fixture parameters"""


@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    return request.param


def test_a(a):
    pass


def idfn(fixture_value):
    if fixture_value == 0:
        return "eggs"
    else:
        return None


def num():
    return [1, 2, 3]


@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    print("#####################", request.param)
    return request.param


def test_data(data_set):
    print(data_set)
    pass


@pytest.fixture(params=num(), ids=idfn)
def b(request):
    return request.param


def test_b(b):
    pass
