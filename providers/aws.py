import subprocess
import yaml
import os

class AWSProvider:
    def __init__(self, credentials=None):
        self.credentials = credentials

    def run_ttp(self, filepath):
        try:
            with open(filepath, 'r') as f:
                data = yaml.safe_load(f)

            print(f"\n[+] TTP: {data.get('name', 'Unnamed')}")
            print(f"[-] Description: {data.get('description', 'No description')}")
            print(f"[-] MITRE Technique: {data.get('mitre_technique', 'N/A')}")
            print(f"[-] Stage: {data.get('stage', 'N/A')}\n")

            steps = data.get('steps', [])
            if not steps:
                print("[!] No steps defined in TTP file.")
                return

            for step in steps:
                action = step.get('action')
                description = step.get('description', 'No description')
                print(f"[>] {description}")
                print(f"    Command: {action}")
                try:
                    subprocess.run(action, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"[!] Command failed: {e}")
                print()
        except FileNotFoundError:
            print(f"[!] File not found: {filepath}")
        except yaml.YAMLError as e:
            print(f"[!] YAML parsing error: {e}")
        except Exception as e:
            print(f"[!] Unexpected error: {e}")