import pytest

from prime import is_prime, generate_prime_array

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

@pytest.mark.parametrize(
        "test_input, result",
        [(0, []),
         (1, [2]),
         (5, [2,3,5,7,11])]
        )
def test_generate_prime_array(test_input, result):
    assert generate_prime_array(test_input) == result
