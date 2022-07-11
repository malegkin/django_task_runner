import time


def fake_task_runner(number: int) -> str:
    time.sleep(5)
    return f'fake result of task with number = {number}'

