# Practice 2

## Table of contents
+ [Compress](#compress)
+ [Diagonal sum](#diagonal-sum)
+ [Merge](#merge)
+ [Squares](#squares)

<a name="compress"><h2>Compress</h2></a>
Сжать строку, заменив подотрезки одинаковых символов на пару <символ, число вхождений>

```python
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
```

<a name="diagonal-sum"><h2>Diagonal sum</h2></a>
Посчитать сумму диагональных элементов матрицы

```python
from typing import List

from hse_python.errors import IllegalArgumentError
from .array_utils import check_any_in_array


def get_matrix_dimensions(matrix: List[List[int]]) -> (int, int):
    n = len(matrix)
    if n == 0:
        return 0, 0

    m = len(matrix[0])
    if check_any_in_array(matrix, lambda x: len(x) != m):
        raise IllegalArgumentError(f"Rows of matrix should have same length")

    return n, m


def diagonal_sum(matrix: List[List[int]]) -> int:
    n, m = get_matrix_dimensions(matrix)
    if n == 0:
        return 0
    if n != m:
        raise IllegalArgumentError(f"Function supports only square matrix, matrix {n}x{m} were given")

    diag_1 = sum(matrix[i][n - 1 - i] for i in range(n))
    diag_2 = sum(matrix[i][i] for i in range(n))
    if n % 2 == 1:
        # diagonals have common element
        return diag_1 + diag_2 - matrix[n // 2][n // 2]
    else:
        return diag_1 + diag_2
```

<a name="merge"><h2>Merge</h2></a>
На входе два отсортированных массива (списка), на выходе получить 1 отсортированный массив.
Элементы списка это целые числа

```python
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
```

<a name="squares"><h2>Squares</h2></a>
Дан отсортированный список в неубавющем порядке.
Вернуть элементы этого списка возведенные в квадрат в неубывающем порядке
Элементы списка это целые числа

```python
from typing import Iterable, List

from hse_python.errors import IllegalArgumentError
from .array_utils import split_array
from .merge import merge, is_sorted


def squared_array(array: Iterable[int]) -> List[int]:
    return [x * x for x in array]


def squares(s: List[int]) -> List[int]:
    if not is_sorted(s):
        raise IllegalArgumentError("Function expects sorted array")
    s1, s2 = split_array(s, lambda x: x > 0)
    return merge(squared_array(reversed(s1)), squared_array(s2))
```