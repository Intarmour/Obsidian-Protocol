import subprocess
import yaml
import os

class OracleProvider:
    def __init__(self, credentials=None, proxy_config=None):
        self.credentials = credentials
        self.proxy_config = proxy_config

    def run_command(self, command):
        env = os.environ.copy()
        if self.proxy_config:
            if "http" in self.proxy_config:
                env["HTTP_PROXY"] = self.proxy_config["http"]
            if "https" in self.proxy_config:
                env["HTTPS_PROXY"] = self.proxy_config["https"]
            if "no_proxy" in self.proxy_config:
                env["NO_PROXY"] = self.proxy_config["no_proxy"]

        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, env=env)
            return result.stdout
        except subprocess.CalledProcessError as e:
            error_msg = f"Error executing Oracle command: {e}"
            print(f"[!] {error_msg}")
            return error_msg
        except Exception as e:
            print(f"[!] Unexpected error in Oracle command: {e}")
            return f"Error executing Oracle command: {e}"

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
                    self.run_command(command)
                except Exception as e:
                    print(f"[!] Command failed: {e}")
        except FileNotFoundError:
            print(f"[!] File not found: {file_path}")
        except yaml.YAMLError as e:
            print(f"[!] YAML parsing error: {e}")