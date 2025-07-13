from typing import Any
from .celery import app
from . import model


@app.task
def run_model(params: dict[str, Any]):
    result = model.run(params)

    return result
