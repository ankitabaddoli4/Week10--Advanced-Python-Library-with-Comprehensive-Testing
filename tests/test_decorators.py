import pytest
from my_advanced_lib.core.decorators import retry, Cache, timer, RetryError


def test_retry_success():
    @retry(max_attempts=3)
    def func():
        return "success"
    assert func() == "success"


def test_retry_failure():
    @retry(max_attempts=2)
    def func():
        raise Exception("fail")

    with pytest.raises(RetryError):
        func()


def test_cache():
    cache = Cache()

    calls = {"count": 0}

    @cache
    def add(x):
        calls["count"] += 1
        return x + 1

    assert add(1) == 2
    assert add(1) == 2
    assert calls["count"] == 1  # cached


def test_timer():
    @timer
    def func():
        return "done"

    assert func() == "done"