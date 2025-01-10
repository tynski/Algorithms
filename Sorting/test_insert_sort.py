import pytest

from insert_sort import insert_sort

@pytest.mark.parametrize(
        "test_input, expected",
        [
            ([1,3,2],[1,2,3]),
            ([5,34,56,1],[1,5,34,56])
        ]
    )
def test_insert_sort(test_input, expected):
    assert insert_sort(test_input) == expected
