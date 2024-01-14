import pytest
import os
from datetime import datetime
from log_message.log_message import log_message
from freezegun import freeze_time


class TestLogMessage:
    def test_create_file(self, set_up_test_data, set_up_test_file):

        log_message(
            file_name=set_up_test_data["file_name"],
            msg_content=set_up_test_data["msg_content"],
            msg_type=set_up_test_data["msg_type"],
        )
        assert os.path.exists(set_up_test_file)

    @pytest.mark.parametrize("msg_type, msg_content", [
        ("DEBUG", "test_msg_1"),
        ("INFO", ""),
        ("WARNING", "123"),
        ("ERROR", "test"),
        ("CRITICAL", "    "),
    ])
    def test_log_to_file(self, set_up_test_data, set_up_test_file, msg_type, msg_content):
        with freeze_time("2024-01-01"):
            current_time = datetime.now()
            timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
            log_message(
                file_name=set_up_test_data["file_name"],
                msg_content=msg_content,
                msg_type=msg_type,
            )

        with open(set_up_test_data["file_name"], 'r') as file:
            file_content = file.readlines()

        expected_log_msg = [f"[{timestamp}][{msg_type}] {msg_content}\n"]

        assert file_content == expected_log_msg
