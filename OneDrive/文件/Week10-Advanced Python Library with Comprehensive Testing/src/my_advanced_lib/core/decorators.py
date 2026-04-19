import time
import functools
import logging
from typing import Callable, TypeVar

T = TypeVar("T")
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class RetryError(Exception):
    pass


def retry(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> T:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.warning(f"Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        raise RetryError("Max retries reached")
                    time.sleep(delay)
        return wrapper
    return decorator


class Cache:
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args):
            if args in self.cache:
                logger.info("Cache hit")
                return self.cache[args]
            result = func(*args)
            self.cache[args] = result
            return result
        return wrapper


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        logger.info(f"{func.__name__} executed in {end-start:.4f}s")
        return result
    return wrapper