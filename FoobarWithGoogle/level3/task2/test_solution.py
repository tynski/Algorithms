from solution import solution

def test_solution():
    assert  solution([1, 2, 3, 4, 5, 6]) == 3

    assert solution([1, 1, 1]) == 1

    assert solution([2,7,8,15,21,24,65,80]) == 2

    assert solution([1, 1, 1, 1]) == 4

    assert solution([1, 1]) == 0

    assert solution([68,234,112,32, 13, 20]) == 0

test_solution()