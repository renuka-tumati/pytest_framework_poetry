import pytest

from helpers.buildtests_utils import test_cases


@pytest.fixture
def builds_scenarios():
    scenario1 = ("iphone_mini", {"name": "mini", "version": "13", "color": "white"})
    scenario2 = ("iphone_pro", {"name": "pro", "version": "14", "color": "gold"})
    scenario3 = ("iphone_mini", {"name": "mini", "version": "13", "color": "white"})
    scenario4 = ("iphone_pro", {"name": "pro", "version": "14", "color": "gold"})
    scenario5 = ("iphone_mini", {"name": "mini", "version": "13", "color": "white"})
    scenario6 = ("iphone_pro", {"name": "pro", "version": "14", "color": "gold"})

    return [scenario1, scenario2, scenario3, scenario4, scenario5, scenario6]


def builds_scenarios_no_fix():
    scenario1 = ("iphone_mini", {"name": "mini", "version": "13", "color": "white"})
    scenario2 = ("iphone_pro", {"name": "pro", "version": "14", "color": "gold"})
    scenario3 = ("iphone_mini", {"name": "mini", "version": "13", "color": "white"})
    scenario4 = ("iphone_pro", {"name": "pro", "version": "14", "color": "gold"})
    scenario5 = ("iphone_mini", {"name": "mini", "version": "13", "color": "white"})
    scenario6 = ("iphone_pro", {"name": "pro", "version": "14", "color": "gold"})

    return [scenario1, scenario2, scenario3, scenario4, scenario5, scenario6]


@pytest.fixture
def builds_scenarios_add_to_list():
    scenario11 = ("basic", {"attribute": "value"})
    scenario22 = ("advanced", {"attribute": "value2"})

    test_cases = [scenario11, scenario22]
    # pytest.tc_list = [scenario11, scenario22]



