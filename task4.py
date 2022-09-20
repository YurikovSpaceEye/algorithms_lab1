def find_opr_3x3(matrix):
    m = matrix
    a1b2c3 = m[0][0] * m[1][1] * m[2][2]
    a3b1c2 = m[2][0] * m[0][1] * m[1][2]
    a2b3c1 = m[1][0] * m[2][1] * m[0][2]
    a3b2c1 = m[2][0] * m[1][1] * m[0][2]
    a1b3c2 = m[0][0] * m[2][1] * m[1][2]
    a2b1c3 = m[1][0] * m[0][1] * m[2][2]

    return a1b2c3 + a3b1c2 + a2b3c1 - a3b2c1 - a1b3c2 - a2b1c3

def find_opr_2x2(matrix):
    m = matrix

    return m[0][0] * m[1][1] - m[1][0] * m[0][1]

def transpose(matrix):
    new_matrix = [[0 for i in range(3)] for i in range(3)]

    for x in range(3):
        for y in range(3):
            new_matrix[y][x] = matrix[x][y]

    return new_matrix

def mask_find(matrix, x, y):
    small = [[0 for i in range(2)] for i in range(2)]

    for x_ in range(3):
        if (x_ == x): continue
        for y_ in range(3):
            if (y_ == y): continue
            xx = x_
            yy = y_

            if (x_ > x): xx-=1
            if (y_ > y): yy-=1

            small[xx][yy] = matrix[x_][y_]

    return find_opr_2x2(small)

def matrix_find_minor(matrix):
    minor = [[0 for i in range(3)] for i in range(3)]

    for x in range(3):
        for y in range(3):
            minor[x][y] = mask_find(matrix, x, y)

    return minor

def matrix_find_algeb_dop(matrix):
    matrix[0][1] = -matrix[0][1]
    matrix[1][0] = -matrix[1][0]
    matrix[1][2] = -matrix[1][2]
    matrix[2][1] = -matrix[2][1]
    return matrix

def matrix_mult_one_to_many(matrix, mult):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            matrix[x][y] *= mult
    return matrix

def find_inverse_3x3_matrix(matrix):
    opr   = find_opr_3x3(matrix)
    minor = matrix_find_minor(matrix)
    alg_dop = matrix_find_algeb_dop(minor)
    alg_dop_t = transpose(alg_dop)
    minor = matrix_mult_one_to_many(alg_dop_t, 1. / opr)

    return minor

# http://mathprofi.ru/kak_naiti_obratnuyu_matricu.html

def test_py():
    find_inverse_3x3_matrix([[2, 5, 7], [6, 3, 4], [5, -2, -3]])

def test_np():
    np.linalg.inv([[2, 5, 7], [6, 3, 4], [5, -2, -3]])

if __name__ == "__main__":
    import timeit
    import numpy as np

    print(timeit.repeat("test_py()", globals=globals(), number=10000))
    print(timeit.repeat("test_np()", globals=globals(), number=10000))