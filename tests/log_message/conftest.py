import pytest
import os


@pytest.fixture()
def set_up_test_data():
    return {
        "file_name": "test_create_file.log",
        "msg_type": "TEST",
        "msg_content": "test_create_file content",
    }


@pytest.fixture()
def set_up_test_file(set_up_test_data: dict | str):
    file_path = os.path.join(os.getcwd(), set_up_test_data["file_name"])
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass
    yield file_path
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass
