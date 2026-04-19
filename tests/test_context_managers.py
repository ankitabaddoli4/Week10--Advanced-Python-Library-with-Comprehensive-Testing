from my_advanced_lib.core.context_managers import SafeFileHandler


def test_safe_file_handler(tmp_path):
    file_path = tmp_path / "test.txt"

    with SafeFileHandler(file_path, "w") as f:
        f.write("hello")

    with open(file_path, "r") as f:
        content = f.read()

    assert content == "hello"