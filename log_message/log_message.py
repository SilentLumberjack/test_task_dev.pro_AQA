import datetime
import os


def log_message(file_name: str, msg_type: str, msg_content: str):
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}][{msg_type}] {msg_content}\n"

    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, file_name)

    with open(file_path, 'a') as log_file:
        log_file.write(log_msg)
