from typing import Iterable, List

from .merge import merge
from .utils import split_array


def squared_array(a: Iterable[int]) -> List[int]:
    return [x * x for x in a]


def squares(s: List[int]) -> List[int]:
    s1, s2 = split_array(s, lambda x: x > 0)
    return merge(squared_array(reversed(s1)), squared_array(s2))
