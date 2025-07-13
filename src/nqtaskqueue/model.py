from typing import Any
import time


def run(params: dict[str, Any]):
    # mock a time consuming run
    time.sleep(5)

    result = {"value": "a mock result"}

    return result
