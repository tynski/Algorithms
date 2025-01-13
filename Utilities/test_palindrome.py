import pytest

from palindrome import palindrome_index, is_palindrome

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

@pytest.mark.parametrize(
        "test_input, expected",
        [("aaa", True),
         ("bbbb", True),
         ("kajawk", False),
         ("kajak", True),
         ("zab", False),
         ("z", True)]
        )
def test_is_palindrome(test_input, expected):
    assert is_palindrome(test_input) == expected
