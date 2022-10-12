# title Helloworld
# description
# Если число делится на 3, вывести hello.
# Если число делится на 5, вывести world.
# Если число делится на 15, вывести helloworld.
# Иначе вывести само число.
# end
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
