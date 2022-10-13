import pytest


@pytest.fixture
def nums():
    return range(10)


def test_nums(nums):
    # Assert
    for i in nums:
        assert i < 10