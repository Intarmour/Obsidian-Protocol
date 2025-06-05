

import subprocess
import yaml

class OracleProvider:
    def __init__(self, credentials=None):
        self.credentials = credentials

    def run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            print(result.stdout)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"[!] Command failed: {e}")
            return str(e)

    def run_ttp(self, file_path):
        print(f"\n[+] Executing Oracle TTP: {file_path}")
        try:
            with open(file_path, 'r') as file:
                ttp = yaml.safe_load(file)

            print(f"\n[+] TTP: {ttp.get('name', 'Unnamed')}")
            print(f"Description: {ttp.get('description', 'No description')}")
            print(f"MITRE Technique: {ttp.get('mitre_technique', 'N/A')}")
            print(f"Stage: {ttp.get('stage', 'N/A')}")

            steps = ttp.get("steps", [])
            if not steps:
                print("[!] No steps defined in TTP.")
                return

            for step in steps:
                description = step.get("description", "No description provided.")
                command = step.get("action", "")
                print(f"\n[*] Step: {description}")
                print(f"[>] Command: {command}")
                try:
                    subprocess.run(command, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"[!] Command failed: {e}")
        except FileNotFoundError:
            print(f"[!] File not found: {file_path}")
        except yaml.YAMLError as e:
            print(f"[!] YAML parsing error: {e}")