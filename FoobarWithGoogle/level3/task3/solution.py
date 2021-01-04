#Hereby solution is utlizing absorbing markow chains

from fractions import Fraction
from fractions import gcd


def solution(m):
    terminal_states = []
    non_terminal_states = []
    R = []
    Q = []

    for i in range(len(m)):
        #transform terminal states into absorbing states or transform numbers into factorials
        row_sum = sum(m[i])
        if row_sum == 0:
            m[i][i] = 1
            terminal_states.append(i)
        else:
            for j in range(len(m[i])):
                m[i][j] = Fraction(m[i][j], row_sum)
            non_terminal_states.append(i)

    if len(terminal_states) == 1:
        return [1, 1]

    for i in non_terminal_states:
        r_row = []
        q_row = []
        for j in range(len(m[i])):
            if j in terminal_states:
                r_row.append(m[i][j])
            else:
                q_row.append(m[i][j])
        R.append(r_row)
        Q.append(q_row)

    identity_matrix = make_identity(len(Q))

    # F = (I - Q) ^ -1
    F = invert_matrix(subtract_matrices(identity_matrix, Q))
    # FR
    FR = multiply_matrices(F, R)
    
    denominator = list_lcm([item.denominator for item in FR[0]])

    result = [item.numerator * denominator / item.denominator for item in FR[0]]

    result.append(denominator)

    return [int(i) for i in result]


def subtract_matrices(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[i])):
            row.append(a[i][j] - b[i][j])
        result.append(row)

    return result


def make_identity(n):
    result = []
    for i in range(n):
        result.append([0] * n)
        result[i][i] = Fraction(1, 1)
    return result


def invert_matrix(m):
    n = len(m)
    assert (len(m) == len(m[0]))
    inverse = make_identity(n)
    for col in range(n):
        diagonal_row = col
        assert (m[diagonal_row][col] != 0)
        k = Fraction(1, m[diagonal_row][col])
        m = multiple_matrix_row(m, diagonal_row, k)
        inverse = multiple_matrix_row(inverse, diagonal_row, k)
        source_row = diagonal_row
        for target_row in range(n):
            if source_row != target_row:
                k = -m[target_row][col]
                m = add_multiplied_row(m, source_row, k, target_row)
                inverse = add_multiplied_row(inverse, source_row, k,
                                             target_row)

    return inverse


def multiple_matrix_row(m, row, k):
    row_operator = make_identity(len(m))
    row_operator[row][row] = k
    return multiply_matrices(row_operator, m)


def multiply_matrices(a, b):
    rows = len(a)
    cols = len(b[0])
    c = [[0] * cols for i in range(rows)]
    for row in range(rows):
        for col in range(cols):
            dot_product = Fraction(0, 1)
            for i in range(len(a[0])):
                dot_product += a[row][i] * b[i][col]
            c[row][col] = dot_product
    return c


def add_multiplied_row(m, source_row, k, target_row):
    # add k * source_row to target_row of matrix m
    row_operator = make_identity(len(m))
    row_operator[target_row][source_row] = k
    return multiply_matrices(row_operator, m)


def list_lcm(list):
    if len(list) == 2:
        return lcm(list[0], list[1])
    elif len(list) > 2:
        return lcm(list[0], list_lcm(list[1:]))


def lcm(x, y):
    return x * y // gcd(x, y)
