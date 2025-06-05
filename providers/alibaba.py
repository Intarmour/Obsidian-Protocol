import subprocess
import yaml

class AlibabaProvider:
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
        try:
            with open(file_path, 'r') as f:
                ttp = yaml.safe_load(f)

            print(f"\n[+] Running Alibaba Cloud TTP: {ttp.get('name', 'Unnamed')}")
            print(f"Description: {ttp.get('description', 'No description')}")
            print(f"MITRE Technique: {ttp.get('mitre_technique', 'N/A')}")
            print(f"Stage: {ttp.get('stage', 'N/A')}\n")

            steps = ttp.get('steps', [])
            if not steps:
                print("[!] No steps defined in TTP.")
                return

            for index, step in enumerate(steps, 1):
                action = step.get("action")
                description = step.get("description", "No description")
                print(f"Step {index}: {description}")
                print(f"Executing: {action}")
                try:
                    subprocess.run(action, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"[!] Command failed: {e}")
                print()
        except Exception as e:
            print(f"[!] Failed to execute Alibaba TTP: {e}")