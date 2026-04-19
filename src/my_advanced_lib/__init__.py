from functools import wraps
import time


# === DECORATORS ===

class RetryError(Exception):
    """Raised when all retry attempts fail."""
    pass

def retry(max_attempts=3):
    """Decorator that retries a function on failure."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise RetryError(f"Failed after {max_attempts} attempts") from e
        return wrapper
    return decorator


class Cache:
    """Simple caching decorator/class."""
    def __init__(self):
        self.cache_dict = {}
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (func.__name__, args, tuple(sorted(kwargs.items())))
            if key not in self.cache_dict:
                self.cache_dict[key] = func(*args, **kwargs)
            return self.cache_dict[key]
        return wrapper


def timer(func):
    """Decorator that prints execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


# === GENERATORS ===

class DataPipeline:
    """Pipeline for processing data through multiple processors."""
    def __init__(self):
        self.processors = []
    
    def add_processor(self, processor):
        """Add a processor function to the pipeline."""
        self.processors.append(processor)
    
    def process(self, data):
        """Process data through all processors."""
        for item in data:
            result = item
            for processor in self.processors:
                result = processor(result)
            yield result


def batch_generator(data, batch_size):
    """Generate batches of data."""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]


def fibonacci_generator():
    """Generate Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# === CONTEXT MANAGERS ===

class SafeFileHandler:
    """Context manager for safe file handling."""
    def __init__(self, file_path, mode='r'):
        self.file_path = file_path
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False


__all__ = [
    'retry',
    'Cache',
    'timer',
    'RetryError',
    'DataPipeline',
    'batch_generator',
    'fibonacci_generator',
    'SafeFileHandler',
]