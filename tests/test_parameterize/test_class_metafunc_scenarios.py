import pytest
from _pytest.python import Metafunc


def pytest_generate_tests(metafunc):
    idlist = []
    argvalues = []
    for scenario in metafunc.cls.scenarios:
        idlist.append(scenario[0])
        items = scenario[1].items()
        argnames = [x[0] for x in items]
        argvalues.append([x[1] for x in items])
    metafunc.parametrize(argnames, argvalues, ids=idlist, scope="class")


scenario1 = ("iphone_mini", {"name": "mini", "version": "13", "color": "white"})
scenario2 = ("iphone_pro", {"name": "pro", "version": "14", "color": "gold"})
scenario3 = ("iphone_mini", {"name": "mini", "version": "13", "color": "white"})
scenario4 = ("iphone_pro", {"name": "pro", "version": "14", "color": "gold"})
scenario5 = ("iphone_mini", {"name": "mini", "version": "13", "color": "white"})
scenario6 = ("iphone_pro", {"name": "pro", "version": "14", "color": "gold"})


class TestSampleWithScenarios:
    scenarios = [scenario1, scenario2, scenario3, scenario4, scenario5, scenario6]

    def test_demo1(self, name, version, color):
        assert isinstance(name, str)
        assert isinstance(version, str)
        assert isinstance(color, str)


scenario11 = ("basic", {"attribute": "value"})
scenario22 = ("advanced", {"attribute": "value2"})


class TestSampleWithScenarios1:
    scenarios = [scenario11, scenario22]

    def test_demo1(self, attribute):
        assert isinstance(attribute, str)

    def test_demo2(self, attribute):
        assert isinstance(attribute, str)
