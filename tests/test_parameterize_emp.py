import pytest

from helpers.json_utils import number_list


@pytest.mark.parametrize("test_input1, test_input2, expected", number_list())
def test_list(test_input1,test_input2, expected):
    assert test_input1+test_input2 == expected









