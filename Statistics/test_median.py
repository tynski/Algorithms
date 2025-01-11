import pytest

from median import median


@pytest.mark.parametrize(
        "test_input, expected",
        [([5,3,1,6,4,2,1],3),
         ([7,5,42,2],6),
         ([5,1,9,6],5.5)])
def test_median(test_input, expected):
    assert median(test_input) == expected
