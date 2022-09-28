from typing import List, Iterator
from .utils import ArrayIterator


class ArraysMinimumIterator(Iterator[int]):
    def __init__(self, arrays: List[List[int]]):
        self.iterators: List[ArrayIterator] = list(map(lambda x: ArrayIterator(x), arrays))

    def __next__(self) -> int:
        if self.is_finished():
            raise StopIteration

        minimum_index = -1
        for i, iterator in enumerate(self.iterators):
            if not iterator.is_finished():
                current_value = iterator.get()
                if minimum_index == -1 or self.iterators[minimum_index].get() > current_value:
                    minimum_index = i
        result = self.iterators[minimum_index].get()
        self.iterators[minimum_index].pop()
        return result

    def is_finished(self):
        return all(map(lambda i: i.is_finished(), self.iterators))


def is_sorted(array: List[int]):
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))


def merge(first: List[int], second: List[int]) -> List[int]:
    if not is_sorted(first) or not is_sorted(second):
        raise RuntimeError("Function expects sorted arrays")
    return list(ArraysMinimumIterator([first, second]))
