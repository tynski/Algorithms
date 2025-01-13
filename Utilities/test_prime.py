import pytest

from prime import is_prime

@pytest.mark.parametrize(
        "test_input, result",
        [(1, False),
         (2, True),
         (3, True),
         (4, False),
         (5, True),
         (6, False),
         (7, True),
         (13, True),
         (21, False),
         (111, False)]
        )
def test_is_prime(test_input, result):
    assert is_prime(test_input) == result
