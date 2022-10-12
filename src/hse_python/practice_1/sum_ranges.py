# title Sum ranges
# description
# Сжать массив чисел, сжав последовательные числа в строку "начало -> конец"
# end
from typing import List

from hse_python.utils.array_utils import ArrayIterator, is_sorted
from hse_python.utils.errors import IllegalArgumentError


def sum_ranges(nums: List[int]) -> List[str]:
    if not is_sorted(nums):
        raise IllegalArgumentError("Function expects sorted array")
    result = []
    iterator = ArrayIterator(nums)
    while not iterator.is_finished():
        start = iterator.get()
        length = 0
        while not iterator.is_finished() and iterator.get() == start + length:
            length += 1
            iterator.pop()
        result.append(f"{start}" if length == 1 else f"{start}->{start + length - 1}")
    return result
