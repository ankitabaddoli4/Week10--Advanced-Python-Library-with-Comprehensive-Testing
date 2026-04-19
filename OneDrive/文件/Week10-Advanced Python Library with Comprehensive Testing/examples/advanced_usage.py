from my_advanced_lib import DataPipeline, fibonacci_generator

def main():
    print("🚀 ADVANCED USAGE")

    pipeline = DataPipeline()
    pipeline.add_processor(lambda x: {**x, "double": x["num"] * 2})

    data = [{"num": 1}, {"num": 2}, {"num": 3}]
    for item in pipeline.process(data):
        print(item)

    print("\nFibonacci:")
    fib = fibonacci_generator()
    for _ in range(5):
        print(next(fib))


if __name__ == "__main__":
    main()