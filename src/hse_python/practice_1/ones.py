# title Ones
# description
# Дан массив, состоящий из 0 и 1
# Найти длину максимального непрерывного отрезка из 1
# end
from typing import List


def ones(binary_list: List[int]) -> int:
    current = 0
    result = 0
    for elem in binary_list:
        if elem == 1:
            current += 1
            result = max(result, current)
        else:
            current = 0
    return result
