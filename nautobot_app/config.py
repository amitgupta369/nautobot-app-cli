import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
DEFAULT_INDEX = BASE_DIR / "index.json"
SYSTEM_INDEX = Path("/etc/nautobot-app/index.json")

def get_index_file(custom_index=None):
    if custom_index:
        return Path(custom_index)
    if SYSTEM_INDEX.exists():
        return SYSTEM_INDEX
    return DEFAULT_INDEX

def load_apps(custom_index=None):
    index_file = get_index_file(custom_index)
    with open(index_file) as f:
        return json.load(f)["apps"]
    return None