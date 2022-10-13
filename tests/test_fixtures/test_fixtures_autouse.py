# contents of test_append.py
import pytest


@pytest.fixture(autouse=True)
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return []


@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)


"""Changes to order inside tests are not cached but changes with in append_first are cached"""
@pytest.mark.order(2)
def test_string_only(order,first_entry):
    order.append("b")
    print(order)
    assert order == [first_entry, "b"]


@pytest.mark.order(1)
def test_string_and_int(order, first_entry):
    order.append(2)
    print(order)
    assert order == [first_entry, 2]


"""Argument cant be assumed by test as deafult argument only nums fixture can run for every method"""


@pytest.fixture(autouse=True)
def nums():
    print()
    return 2


@pytest.mark.order(3)
def test_nums_only(order):
    order.append("b")
    print(order)
    print(nums)
    assert len(order) == nums


@pytest.mark.order(4)
def test_string_nums(order, nums):
    order.append(2)
    print(order)
    assert len(order) == nums

