from pathlib import Path
from typing import Any
from celery import Celery
from .config import DATA_DIR

# broker directories
BROKER_DIRS = {
    "data_folder_in": DATA_DIR / "in",
    "data_folder_out": DATA_DIR / "in",
    "processed_folder": DATA_DIR / "processed",
}
for folder in BROKER_DIRS.values():
    folder.mkdir(parents=True, exist_ok=True)
BROKER_DIRS["store_processed"] = True

# backend directory
BACKEND_DIR = DATA_DIR / "results"
BACKEND_DIR.mkdir(parents=True, exist_ok=True)


class CeleryConfig:
    """Configuration for Celery broker and results."""

    broker_url: str = "filesystem://localhost"
    broker_transport_options: dict[str, Any] = {
        k: str(f) if isinstance(f, Path) else f for k, f in BROKER_DIRS.items()
    }

    result_backend: str = f"file://{BACKEND_DIR}"

    task_serializer: str = "json"
    result_serializer: str = "json"
    persis_results: bool = True
    accept_content: list[str] = ["json"]
    imports: tuple[str] = ("nqtaskqueue.tasks",)


app = Celery("nqtaskqueue")
app.config_from_object(CeleryConfig)
