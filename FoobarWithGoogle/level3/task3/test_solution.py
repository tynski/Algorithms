from solution import solution


def test_solution():
    #sanity check FG sum of each row should return 1
    assert solution([[0, 2, 1, 0, 0], 
                    [0, 0, 0, 3, 4], 
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0]]) == [7, 6, 8, 21]
    assert solution([[0, 1, 0, 0, 0, 1], 
                    [4, 0, 0, 3, 2,0], 
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]]) == [0, 3, 2, 9, 14]

    assert solution([[0]]) == [1 ,1]
