import pytest


@pytest.fixture
def sample_data():
    return [{"id": 1}, {"id": 2}, {"id": 3}]


@pytest.fixture
def sample_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello\nWorld")
    return file