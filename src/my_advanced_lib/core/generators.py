from typing import Iterator, Callable


class DataPipeline:
    def __init__(self):
        self.processors = []

    def add_processor(self, func: Callable):
        self.processors.append(func)
        return self

    def process(self, data: list[dict]) -> Iterator[dict]:
        for item in data:
            for p in self.processors:
                item = p(item)
            yield item


def batch_generator(data, batch_size=2):
    batch = []
    for item in data:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b