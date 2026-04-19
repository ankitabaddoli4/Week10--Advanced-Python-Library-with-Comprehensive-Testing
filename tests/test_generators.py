from my_advanced_lib.core.generators import (
    DataPipeline,
    batch_generator,
    fibonacci_generator,
)


def test_pipeline(sample_data):
    pipeline = DataPipeline()
    pipeline.add_processor(lambda x: {**x, "ok": True})

    result = list(pipeline.process(sample_data))
    assert result[0]["ok"] is True


def test_batch_generator():
    data = [1, 2, 3, 4, 5]
    batches = list(batch_generator(data, 2))

    assert batches == [[1, 2], [3, 4], [5]]


def test_fibonacci():
    fib = fibonacci_generator()
    result = [next(fib) for _ in range(5)]
    assert result == [0, 1, 1, 2, 3]