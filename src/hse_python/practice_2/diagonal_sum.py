# title Diagonal sum
# description
# Посчитать сумму диагональных элементов матрицы
# end
from typing import List

from hse_python.errors import IllegalArgumentError
from .array_utils import check_any_in_array


def get_matrix_dimensions(matrix: List[List[int]]) -> (int, int):
    n = len(matrix)
    if n == 0:
        return 0, 0

    m = len(matrix[0])
    if check_any_in_array(matrix, lambda x: len(x) != m):
        raise IllegalArgumentError(f"Rows of matrix should have same length")

    return n, m


def diagonal_sum(matrix: List[List[int]]) -> int:
    n, m = get_matrix_dimensions(matrix)
    if n == 0:
        return 0
    if n != m:
        raise IllegalArgumentError(f"Function supports only square matrix, matrix {n}x{m} were given")

    diag_1 = sum(matrix[i][n - 1 - i] for i in range(n))
    diag_2 = sum(matrix[i][i] for i in range(n))
    if n % 2 == 1:
        # diagonals have common element
        return diag_1 + diag_2 - matrix[n // 2][n // 2]
    else:
        return diag_1 + diag_2
