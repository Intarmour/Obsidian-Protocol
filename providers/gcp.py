import os
import subprocess
import yaml
from dotenv import load_dotenv

load_dotenv()

def execute_gcp_ttp(yaml_file):
    print(f"Executing GCP TTP from: {yaml_file}")

    if not os.path.exists(yaml_file):
        print(f"File not found: {yaml_file}")
        return

    with open(yaml_file, 'r') as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML: {exc}")
            return

    steps = data.get("steps", [])
    if not steps:
        print("No steps defined in the TTP file.")
        return

    for idx, step in enumerate(steps):
        action = step.get("action", "")
        description = step.get("description", "")

        print(f"\n[{idx+1}] {description}")
        print(f"Command: {action}")

        try:
            subprocess.run(action, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Step failed: {e}")
            continue

    print("\nGCP TTP execution completed.")