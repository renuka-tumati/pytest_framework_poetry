import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )
    parser.addoption("--all", action="store_true", help="run all combinations")


def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))


def test_inside_outer_conf():
    assert True


@pytest.fixture
def username():
    print("\n tests conftest fixture")
    return 'username'


def test_username(username):
    assert username == 'username'
