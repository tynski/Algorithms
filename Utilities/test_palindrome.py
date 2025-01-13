import pytest

from palindrome import palindrome_index

@pytest.mark.parametrize(
        "test_input, expected",
        [("aaa",-1),
         ("bbbb",-1),
         ("kajawk",4),
         ("kawjak",2),
         ("z", -1)]
        )
def test_palindrome_index(test_input, expected):
    assert palindrome_index(test_input) == expected
