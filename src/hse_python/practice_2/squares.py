from typing import Iterable, List, Callable
from .merge import merge


def squared(a: Iterable[int]) -> List[int]:
    return list(map(lambda x: x * x, a))


def split(array: List[int], predicate: Callable[[int], bool]) -> (List[int], List[int]):
    truth_array = []
    lie_array = []
    for elem in array:
        if predicate(elem):
            truth_array.append(elem)
        else:
            lie_array.append(elem)
    return lie_array, truth_array


def squares(s: List[int]) -> List[int]:
    s1, s2 = split(s, lambda x: x > 0)
    return merge(squared(reversed(s1)), squared(s2))
