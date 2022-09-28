from typing import List


def get_matrix_dimensions(matrix: List[List[int]]) -> (int, int):
    n = len(matrix)
    if n == 0:
        return 0, 0

    m = len(matrix[0])
    if any(map(lambda x: len(x) != m, matrix)):
        raise RuntimeError(f"Rows of matrix should have same length")

    return n, m


def diagonal_sum(matrix: List[List[int]]) -> int:
    n, m = get_matrix_dimensions(matrix)
    if n == 0:
        return 0
    if n != m:
        raise RuntimeError(f"Function supports only square matrix, matrix {n}x{m} were given")

    diag_1 = sum(matrix[i][n - 1 - i] for i in range(n))
    diag_2 = sum(matrix[i][i] for i in range(n))
    if n % 2 == 1:
        # diagonals have common element
        return diag_1 + diag_2 - matrix[n // 2][n // 2]
    else:
        return diag_1 + diag_2
