import time
from logging import Logger
from typing import NamedTuple, Callable


class Task(NamedTuple):
    title: str
    description: str
    code: str


def measure_time(logger: Logger):
    def logged_function(func: Callable):
        def wrapped(*args):
            start = time.time()
            res = func(*args)
            end = time.time()
            logger.debug(f"Function `{func.__name__}` took " + str(round((end - start) * 1000)) + " ms")
            return res
        return wrapped
    return logged_function
