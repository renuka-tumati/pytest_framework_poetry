import pytest
from _pytest.python import Metafunc
from fixtures.cases_build import *
from helpers.buildtests_utils import test_cases


def pytest_generate_tests(metafunc):
    idlist = []
    argvalues = []
    for scenario in metafunc.cls.scenarios:
        idlist.append(scenario[0])
        items = scenario[1].items()
        argnames = [x[0] for x in items]
        argvalues.append([x[1] for x in items])
    metafunc.parametrize(argnames, argvalues, ids=idlist, scope="class")


class TestSampleWithScenarios:
    scenarios = builds_scenarios_no_fix()

    def test_demo1(self, name, version, color):
        assert isinstance(name, str)
        assert isinstance(version, str)
        assert isinstance(color, str)


@pytest.mark.usefixtures("builds_scenarios_add_to_list")
class TestSampleWithScenarios1:
    scenarios = test_cases
    # scenarios = pytest.tc_list

    def test_demo1(self, attribute):
        assert isinstance(attribute, str)

    def test_demo2(self, attribute):
        assert isinstance(attribute, str)

