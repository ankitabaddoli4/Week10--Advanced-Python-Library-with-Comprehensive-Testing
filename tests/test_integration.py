import pytest
from my_advanced_lib import retry, Cache, DataPipeline


def test_full_integration():
    """
    Integration test:
    Combines retry decorator, cache decorator, and data pipeline.
    """

    cache = Cache()

    @retry(max_attempts=2)
    @cache
    def process(x):
        return x * 2

    pipeline = DataPipeline()
    pipeline.add_processor(lambda x: {"value": process(x)})

    data = [1, 2, 3]

    result = list(pipeline.process(data))

    assert result == [
        {"value": 2},
        {"value": 4},
        {"value": 6}
    ]


def test_cache_with_pipeline():
    """
    Ensures cache works inside pipeline
    """

    cache = Cache()
    call_count = {"count": 0}

    @cache
    def process(x):
        call_count["count"] += 1
        return x * 10

    pipeline = DataPipeline()
    pipeline.add_processor(lambda x: {"value": process(x)})

    data = [1, 1, 1]

    result = list(pipeline.process(data))

    assert result == [
        {"value": 10},
        {"value": 10},
        {"value": 10}
    ]

    # Should only call once due to caching
    assert call_count["count"] == 1


def test_retry_integration():
    """
    Tests retry decorator behavior inside integration
    """

    attempts = {"count": 0}

    @retry(max_attempts=3)
    def flaky_function():
        attempts["count"] += 1
        if attempts["count"] < 2:
            raise Exception("Temporary failure")
        return "success"

    result = flaky_function()

    assert result == "success"
    assert attempts["count"] == 2