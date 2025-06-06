

import yaml
import os
import sys

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.yaml")

REQUIRED_FIELDS = {
    "default_provider": str,
    "log_format": str,
    "proxy_enabled": bool,
    "proxy_url": str,
    "output_format": str
}

def validate_config(path):
    if not os.path.exists(path):
        print(f"[ERROR] Config file not found at {path}")
        return False

    with open(path, "r") as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"[ERROR] YAML parsing error: {e}")
            return False

    missing = []
    for field, ftype in REQUIRED_FIELDS.items():
        if field not in config:
            missing.append(field)
        elif not isinstance(config[field], ftype):
            print(f"[ERROR] Field '{field}' has incorrect type (expected {ftype.__name__})")
            return False

    if missing:
        print(f"[ERROR] Missing required config fields: {', '.join(missing)}")
        return False

    print("[OK] config.yaml is valid.")
    return True

if __name__ == "__main__":
    success = validate_config(CONFIG_PATH)
    sys.exit(0 if success else 1)