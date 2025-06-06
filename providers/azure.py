import subprocess
import yaml
import os

class AzureProvider:
    def __init__(self, credentials=None, proxy_config=None):
        self.credentials = credentials
        self.proxy_config = proxy_config or {}

    def run_command(self, command):
        env = os.environ.copy()
        if self.proxy_config.get("http"):
            env["http_proxy"] = self.proxy_config["http"]
        if self.proxy_config.get("https"):
            env["https_proxy"] = self.proxy_config["https"]

        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, env=env)
            print(result.stdout)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"[!] Command failed: {e}")
            return str(e)

    def run_ttp(self, file_path):
        print(f"\n[+] Executing Azure TTP: {file_path}")
        try:
            with open(file_path, 'r') as file:
                ttp = yaml.safe_load(file)

            print(f"\n[+] TTP: {ttp.get('name', 'Unnamed')}")
            print(f"Description: {ttp.get('description', 'No description')}")
            print(f"MITRE Technique: {ttp.get('mitre_technique', 'N/A')}")
            print(f"Stage: {ttp.get('stage', 'N/A')}")

            for step in ttp.get("steps", []):
                description = step.get("description", "No description provided.")
                command = step.get("action", "")
                print(f"\n[*] Step: {description}")
                print(f"[>] Command: {command}")

                try:
                    self.run_command(command)
                except Exception as e:
                    print(f"[!] Command failed: {e}")

        except FileNotFoundError:
            print(f"[!] TTP file not found: {file_path}")
        except yaml.YAMLError as e:
            print(f"[!] YAML parsing error: {e}")