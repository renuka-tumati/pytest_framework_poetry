import pytest
from _pytest.python import Metafunc


@pytest.fixture()
def nums_fixture():
    return [(3+5, 8, 16), (2+4, 6, 12), (6*9, 42, 96)]


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("test_input1,test_input2, expected", [(3+5, 8, 16), (2+4, 6, 12), (6*9, 42, 96)])
def test_3params(test_input1,test_input2, expected):
    assert test_input1+test_input2 == expected


nums = [(3+5, 8, 16), (2+4, 6, 12), (6*9, 42, 96)]


@pytest.mark.parametrize("test_input1, test_input2, expected", nums)
def test_list(test_input1,test_input2, expected):
    assert test_input1+test_input2 == expected


"""
@pytest.mark.skip
@pytest.mark.parametrize("test_input1, test_input2, expected", nums_fixture)
def test_list_fix(test_input1,test_input2, expected):
    assert test_input1+test_input2 == expected """



def pytest_generate_tests(metafunc: Metafunc) -> None:
    if (
        "test_inputa" in metafunc.fixturenames and
        "test_inputb" in metafunc.fixturenames and
        "expectedc" in metafunc.fixturenames
    ):

        params = [(3+5, 8, 16), (2+4, 6, 12), (6*9, 42, 96)]
        metafunc.parametrize(
            argnames=["test_inputa", "test_inputb", "expectedc"],
            argvalues=params,
            ids=["8+8=16", "6+6=12", "54+42!=95"]

        )


def test_list_metafunc(test_inputa: int, test_inputb: int, expectedc: int) -> None:
    assert test_inputa+test_inputb == expectedc


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3+5", 8),
        pytest.param("1+7", 8, marks=pytest.mark.basic),
        pytest.param("2+4", 6, marks=pytest.mark.basic, id="basic_2+4"),
        pytest.param(
            "6*9", 42, marks=[pytest.mark.basic, pytest.mark.xfail], id="basic_6*9"
        ),
    ],
)
def test_eval_mark(test_input, expected):
    assert eval(test_input) == expected






