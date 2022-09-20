import numpy as np

def transpose_matrix(matrix: np.matrix):
    return matrix.transpose([1, 0])

def matrix_multiply(matrix1: np.matrix, matrix2: np.matrix):
    return matrix1 * matrix2

def matrix_find_rank(matrix: np.matrix):
    return np.linalg.matrix_rank(matrix)

if __name__ == "__main__":
    matrix1 = [i for i in range(10)]
    matrix2 = [[i for i in range(10)] for i in range(10)]
    matrix3 = [[i for i in range(5)] for i in range(10)]

    matrix5 = [[i for i in range(10)] for i in range(5)]
    matrix6 = [[i for i in range(5)] for i in range(10)]


    matrix4 = matrix_multiply(np.matrix(matrix2), np.matrix(matrix3))
    print(matrix4)
    print("----------")
    matrix7 = matrix_multiply(np.matrix(matrix5), np.matrix(matrix6))
    print(matrix7)

    print(matrix_find_rank(np.matrix(matrix4)))


    matrix__ = [[10, 20, 10], [20, 40, 20], [30, 50, 0]]
    print(matrix_find_rank(np.matrix(matrix__)))
    # print(matrix_find_rank([[10, 20, 10], [-20, -30, 10], [30, 50, 0]]))