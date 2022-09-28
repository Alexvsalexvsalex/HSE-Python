from typing import List
from .utils import ArrayIterator


def compress(s: List[str]) -> str:
    if any(map(lambda x: len(x) != 1, s)):
        raise RuntimeError("Function expects list of symbols")
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
