# title Merge
# description
# На входе два отсортированных массива (списка), на выходе получить 1 отсортированный массив.
# Элементы списка это целые числа
# end
from typing import List, Generator

from hse_python.errors import IllegalArgumentError
from .array_utils import ArrayIterator, check_all_in_array


def merge_generator(*arrays: List[int]) -> Generator[int, None, None]:
    iterators = [ArrayIterator(x) for x in arrays]
    while not check_all_in_array(iterators, lambda x: x.is_finished()):
        minimum_index = -1
        for i, iterator in enumerate(iterators):
            if not iterator.is_finished():
                current_value = iterator.get()
                if minimum_index == -1 or iterators[minimum_index].get() > current_value:
                    minimum_index = i
        yield iterators[minimum_index].pop()


def is_sorted(array: List[int]) -> bool:
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))


def merge(first: List[int], second: List[int]) -> List[int]:
    if not is_sorted(first) or not is_sorted(second):
        raise IllegalArgumentError("Function expects sorted arrays")
    return list(merge_generator(first, second))