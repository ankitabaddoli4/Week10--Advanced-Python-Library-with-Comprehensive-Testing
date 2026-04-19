from my_advanced_lib import retry, Cache, timer, DataPipeline, batch_generator
import random

cache = Cache()

@retry(max_attempts=3)
@timer
@cache
def fetch_data(url: str):
    if random.random() < 0.5:
        raise Exception("API failed")
    return {"data": "sample", "url": url}


def run_demo():
    print("⚡ ADVANCED PYTHON LIBRARY DEMO\n")

    print("🔧 DECORATORS DEMO:")
    result = fetch_data("https://api.test.com")
    print(result)

    print("\n🔄 GENERATORS DEMO:")
    pipeline = DataPipeline()
    pipeline.add_processor(lambda x: {**x, "processed": True})

    data = [{"id": 1}, {"id": 2}]
    for item in pipeline.process(data):
        print(item)

    print("\n📦 BATCH PROCESSING:")
    for batch in batch_generator(range(5), 2):
        print(batch)


if __name__ == "__main__":
    run_demo()