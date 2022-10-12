# Practice 1

## Table of contents
+ [Helloworld](#helloworld)
+ [Ones](#ones)
+ [Sum ranges](#sum-ranges)

<a name="helloworld"><h2>Helloworld</h2></a>
Если число делится на 3, вывести hello.
Если число делится на 5, вывести world.
Если число делится на 15, вывести helloworld.
Иначе вывести само число.

### Solution:
```python
from typing import List


def helloworld(n: int) -> List[str]:
    res = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            res.append('helloworld')
        elif i % 3 == 0:
            res.append('hello')
        elif i % 5 == 0:
            res.append('world')
        else:
            res.append(str(i))
    return res
```

<a name="ones"><h2>Ones</h2></a>
Дан массив, состоящий из 0 и 1
Найти длину максимального непрерывного отрезка из 1

### Solution:
```python
from typing import List


def ones(binary_list: List[int]) -> int:
    current = 0
    result = 0
    for elem in binary_list:
        if elem == 1:
            current += 1
            result = max(result, current)
        else:
            current = 0
    return result
```

<a name="sum-ranges"><h2>Sum ranges</h2></a>
Сжать массив чисел, сжав последовательные числа в строку "начало -> конец"

### Solution:
```python
from typing import List

from hse_python.utils.array_utils import ArrayIterator, is_sorted
from hse_python.utils.errors import IllegalArgumentError


def sum_ranges(nums: List[int]) -> List[str]:
    if not is_sorted(nums):
        raise IllegalArgumentError("Function expects sorted array")
    result = []
    iterator = ArrayIterator(nums)
    while not iterator.is_finished():
        start = iterator.get()
        length = 0
        while not iterator.is_finished() and iterator.get() == start + length:
            length += 1
            iterator.pop()
        result.append(f"{start}" if length == 1 else f"{start}->{start + length - 1}")
    return result
```