import pytest
from _pytest.python import Metafunc


# pytest -q --stringinput="hello" --stringinput="world" test_strings.py
def test_valid_string(stringinput):
    assert stringinput.isalpha()


def test_compute(param1, param2):
    assert param1 == param2


def test_compute2(param1, param2):
    assert param1 == param2


def test_multi_case_generation(param4, param3):
    assert param3 == param4


def id_func(val):
    """ Every value in tuple is passed to val, so can skip anything not needed """
    print(val)
    return str(val) + "RT"


def pytest_generate_tests(metafunc):
    """pytest tests/Test_param_with_id.py --collect-only  - this will display the test ids"""
    if "param1" in metafunc.fixturenames or "param2" in metafunc.fixturenames:

        """Externalize the data and use utils to return list of tuples"""
        arg_list = [(4, 4), (3, 3), (2, 2)]
        """ Can create Id list along with arg list generator util so the number of args and ids will be in sync"""
        id_list = [ "case1", "case2", "case3"]
        if metafunc.config.getoption("all"):
            end = 5
        else:
            end = 4

        metafunc.parametrize(
            argnames=["param1", "param2"],
            argvalues=arg_list,
            # ids = id_list
            ids=id_func
        )

    if "param3" in metafunc.fixturenames and "param4" in metafunc.fixturenames:

        """Externalize the data and use utils to return list of tuples"""
        arg_list1 = [(4, 4), (3, 3), (2, 2)]
        """ Can create Id list along with arg list generator util so the number of args and ids will be in sync"""
        id_list1 = ["a", "b", "c"]
        metafunc.parametrize(
            argnames=["param3", "param4"],
            argvalues=arg_list1,
            ids = id_list1
        )


