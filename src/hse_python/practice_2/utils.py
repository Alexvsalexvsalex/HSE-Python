from typing import Iterator, List, Callable, TypeVar, Optional

T = TypeVar('T')


class ArrayIterator(Iterator[T]):
    def __init__(self, array: List[T]):
        self.i: int = 0
        self.array: List[T] = array

    def get(self) -> Optional[T]:
        if self.is_finished():
            return None
        return self.array[self.i]

    def pop(self) -> Optional[T]:
        if self.is_finished():
            return None
        result = self.get()
        self.i += 1
        return result

    def __next__(self) -> Optional[T]:
        if self.is_finished():
            raise StopIteration
        return self.pop()

    def is_finished(self) -> bool:
        return self.i >= len(self.array)


def check_any_in_array(array: List[T], predicate: Callable[[T], bool]) -> bool:
    return any(map(predicate, array))


def check_all_in_array(array: List[T], predicate: Callable[[T], bool]) -> bool:
    return all(map(predicate, array))


def split_array(array: List[T], predicate: Callable[[T], bool]) -> (List[T], List[T]):
    truth_array = []
    lie_array = []
    for elem in array:
        if predicate(elem):
            truth_array.append(elem)
        else:
            lie_array.append(elem)
    return lie_array, truth_array
