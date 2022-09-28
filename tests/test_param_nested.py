import pytest
from _pytest.python import Metafunc


# pytest -q --stringinput="hello" --stringinput="world" test_strings.py
def test_valid_string(stringinput):
    assert stringinput.isalpha()


def test_compute(param1, param2):
    assert param1 == param2


def test_compute2(param1, param2):
    assert param1 == param2

""" Not able to load single param of configuration from metafunc
In test_compute3: function uses no argument 'param2'
def test_compute3(param1):
    assert param1 < 5
"""



def pytest_generate_tests(metafunc):
    if "param1" in metafunc.fixturenames or "param2" in metafunc.fixturenames:

        if metafunc.config.getoption("all"):
            end = 5
        else:
            end = 4
        metafunc.parametrize("param1", range(end))
        metafunc.parametrize("param2", range(end))