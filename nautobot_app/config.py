import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
INDEX_FILE = BASE_DIR / "index.json"


def load_apps():
    with open(INDEX_FILE) as f:
        return json.load(f)["apps"]