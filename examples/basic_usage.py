from my_advanced_lib import retry, Cache, timer, DataPipeline

cache = Cache()

@retry(max_attempts=3)
@timer
@cache
def fetch_data(x):
    return {"value": x}


def main():
    print("🔹 BASIC USAGE")

    print(fetch_data(10))
    print(fetch_data(10))  # cache hit

    pipeline = DataPipeline()
    pipeline.add_processor(lambda x: {**x, "processed": True})

    data = [{"id": 1}, {"id": 2}]
    for item in pipeline.process(data):
        print(item)


if __name__ == "__main__":
    main()
