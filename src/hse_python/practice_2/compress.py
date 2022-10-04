from typing import List

from hse_python.errors import IllegalArgumentError
from .array_utils import ArrayIterator, check_any_in_array


def compress(s: List[str]) -> str:
    if check_any_in_array(s, lambda x: len(x) != 1):
        raise IllegalArgumentError("Function expects list of symbols")
    chunks = []
    iterator = ArrayIterator(s)
    while not iterator.is_finished():
        c = iterator.get()
        length = 0
        while not iterator.is_finished() and iterator.get() == c:
            length += 1
            iterator.pop()
        chunks.append(f"{c}" if length == 1 else f"{c}{length}")
    return "".join(chunks)
