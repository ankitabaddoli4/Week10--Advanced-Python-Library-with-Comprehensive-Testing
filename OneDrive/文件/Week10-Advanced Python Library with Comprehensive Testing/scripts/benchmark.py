import time
from my_advanced_lib import Cache

cache = Cache()

@cache
def compute(x):
    time.sleep(0.5)
    return x * x

start = time.time()
compute(10)
print("First:", time.time() - start)

start = time.time()
compute(10)
print("Cached:", time.time() - start)