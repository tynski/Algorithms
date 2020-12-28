from solution import solution

def test_solution():
    assert  solution([1, 2, 3, 4, 5, 6]) == 3

    assert solution([1, 1, 1]) == 1

test_solution()