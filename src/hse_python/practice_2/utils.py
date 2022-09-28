from typing import Iterator


class ArrayIterator(Iterator):
    def __init__(self, array):
        self.i: int = 0
        self.array = array

    def get(self):
        if self.is_finished():
            return None
        return self.array[self.i]

    def pop(self):
        if not self.is_finished():
            self.i += 1

    def __next__(self):
        if self.is_finished():
            raise StopIteration
        result = self.get()
        self.pop()
        return result

    def is_finished(self) -> bool:
        return self.i >= len(self.array)
