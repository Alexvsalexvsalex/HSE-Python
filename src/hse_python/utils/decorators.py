import time
from logging import Logger
from typing import Callable


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


def async_measure_time(logger: Logger):
    def logged_function(func: Callable):
        async def wrapped(*args):
            start = time.time()
            res = await func(*args)
            end = time.time()
            logger.debug(f"Async function `{func.__name__}` took " + str(round((end - start) * 1000)) + " ms")
            return res
        return wrapped
    return logged_function
