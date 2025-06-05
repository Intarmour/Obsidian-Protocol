import os
import subprocess
import yaml
from dotenv import load_dotenv

load_dotenv()

class GCPProvider:
    def __init__(self, credentials=None):
        self.credentials = credentials

    def run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            print(result.stdout)
            return result.stdout
        except subprocess.CalledProcessError as e:
            error_msg = f"Error executing GCP command: {e}"
            print(error_msg)
            return error_msg

    def run_ttp(self, yaml_file):
        print(f"\n[+] Executing GCP TTP: {yaml_file}")

        if not os.path.exists(yaml_file):
            print(f"[!] File not found: {yaml_file}")
            return

        try:
            with open(yaml_file, 'r') as file:
                data = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"[!] Error parsing YAML: {exc}")
            return

        print(f"\n[+] TTP: {data.get('name', 'Unnamed')}")
        print(f"Description: {data.get('description', 'No description')}")
        print(f"MITRE Technique: {data.get('mitre_technique', 'N/A')}")
        print(f"Stage: {data.get('stage', 'N/A')}")

        steps = data.get("steps", [])
        if not steps:
            print("[!] No steps defined in the TTP file.")
            return

        for idx, step in enumerate(steps):
            action = step.get("action", "")
            description = step.get("description", "No description provided.")

            print(f"\n[{idx+1}] {description}")
            print(f"[>] Command: {action}")

            try:
                subprocess.run(action, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"[!] Step failed: {e}")
                continue

        print("\n[+] GCP TTP execution completed.")