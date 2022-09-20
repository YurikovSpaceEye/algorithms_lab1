import copy

def check_if_matrix(matrix):
    try:
        first_size = len(matrix[0])
        for element in matrix:
            if (len(element) != first_size):
                return False
        return True
    except:
        for element in matrix:
            if not (type(element) == int or type(element) == float):
                return False
        return True

def get_size(matrix):
    if not check_if_matrix(matrix):
        raise Exception("Не матрица")

    try:
        return (len(matrix), len(matrix[0]))
    except:
        return (len(matrix), 0)


def transpose_matrix(matrix):
    width, height = get_size(matrix)
    if (height == 0):
        return matrix

    new_matrix = [[0 for i in range(width)] for i in range(height)]

    for x in range(width):
        for y in range(height):
            new_matrix[y][x] = matrix[x][y]

    return new_matrix

def display_matrix(matrix):
    width, height = get_size(matrix)
    if (height == 0):
        print(matrix)
        return

    for i in range(len(matrix)):
        submatrix = matrix[i]
        if (i == 0):
            print("[", end="")
            print(submatrix)
        elif i != len(matrix)-1:
            print(" ", end="")
            print(submatrix)
        else:
            print(" ", end="")
            print(submatrix, end="]\n")

def elementwise_mult(arr1, arr2):
    new_arr = [0 for i in range(len(arr1))]
    for i, (el1, el2) in enumerate(zip(arr1, arr2)):
        new_arr[i] = el1 * el2

    return new_arr

def matrix_multiply(matrix1, matrix2):
    width1, height1 = get_size(matrix1)
    width2, height2 = get_size(matrix2)

    if (height1 != width2):
        raise Exception("Не согласованные матрицы")

    new_matrix = [[0 for i in range(height2)] for i in range(width1)]

    matrix2 = transpose_matrix(matrix2)

    for x in range(width1):
        row = matrix1[x]
        for y in range(height2):
            col = matrix2[y]

            new_matrix[x][y] = sum(elementwise_mult(row, col))

    return new_matrix

def matrix_swap(matrix, row1, row2, col):
    for i in range(col):
        temp = matrix[row1][i]
        matrix[row1][i] = matrix[row2][i]
        matrix[row2][i] = temp

#https://www.geeksforgeeks.org/program-for-rank-of-matrix/
def matrix_find_rank(matrix):
    a = copy.deepcopy(matrix)
    r, c = get_size(a)

    rank = c

    for row in range(0, rank, 1):
        if a[row][row] != 0:
            for col in range(0, r, 1):
                if col != row:
                    multiplier = a[col][row] / a[row][row]
                    for i in range(rank):
                        a[col][i] -= (multiplier * a[row][i])
        else:
            reduce = True

            for i in range(row+1, r, 1):
                if a[i][row] != 0:
                    matrix_swap(a, row, i, rank)
                    reduce = False
                    break

            if reduce:
                rank -= 1
                for i  in range(0, r, 1):
                    a[i][row] = a[i][rank]

            row -= 1
    return rank

if __name__ == "__main__":
    matrix1 = [i for i in range(10)]
    matrix2 = [[i for i in range(10)] for i in range(10)]
    matrix3 = [[i for i in range(5)] for i in range(10)]

    matrix5 = [[i for i in range(10)] for i in range(5)]
    matrix6 = [[i for i in range(5)] for i in range(10)]


    matrix4 = matrix_multiply(matrix2, matrix3)
    display_matrix(matrix4)
    print("----------")
    matrix7 = matrix_multiply(matrix5, matrix6)
    display_matrix(matrix7)

    print(matrix_find_rank(matrix4))