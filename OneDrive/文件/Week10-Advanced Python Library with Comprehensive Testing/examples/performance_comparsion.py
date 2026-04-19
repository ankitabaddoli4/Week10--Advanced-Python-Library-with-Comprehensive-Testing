import time
from my_advanced_lib import Cache

cache = Cache()

@cache
def slow_function(x):
    time.sleep(1)
    return x * 2


def main():
    print("⏱ PERFORMANCE TEST")

    start = time.time()
    print(slow_function(5))
    print("First call:", time.time() - start)

    start = time.time()
    print(slow_function(5))
    print("Second call (cached):", time.time() - start)


if __name__ == "__main__":
    main()