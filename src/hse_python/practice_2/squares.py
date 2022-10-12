# title Squares
# description
# Дан отсортированный список в неубавющем порядке.
#
# Вернуть элементы этого списка возведенные в квадрат в неубывающем порядке
#
# Элементы списка это целые числа
# end
from typing import Iterable, List

from hse_python.utils.errors import IllegalArgumentError
from hse_python.utils.array_utils import split_array, is_sorted
from .merge import merge


def squared_array(array: Iterable[int]) -> List[int]:
    return [x * x for x in array]


def squares(s: List[int]) -> List[int]:
    if not is_sorted(s):
        raise IllegalArgumentError("Function expects sorted array")
    s1, s2 = split_array(s, lambda x: x > 0)
    return merge(squared_array(reversed(s1)), squared_array(s2))
