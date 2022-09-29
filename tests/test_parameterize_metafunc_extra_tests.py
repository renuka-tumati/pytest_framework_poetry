import pytest
from _pytest.python import Metafunc


def test_compute(param1, param2):
    assert param1 == param2


def test_compute2(param2):
    assert param2 < 100


def test_compute3(param3):
    assert param3 < 100
""" Not able to load single param of configuration from metafunc
In test_compute3: function uses no argument 'param2'
def test_compute3(param1):
    assert param1 < 5
"""


def pytest_generate_tests(metafunc):
    if "param1" in metafunc.fixturenames:
        metafunc.parametrize("param1", range(2))
    if "param2" in metafunc.fixturenames:
        metafunc.parametrize("param2", range(2))


def pytest_generate_tests_1(metafunc):
    if "param3" in metafunc.fixturenames:
        metafunc.parametrize("param3", range(2))

