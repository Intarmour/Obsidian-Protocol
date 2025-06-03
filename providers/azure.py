import subprocess
import yaml

def execute_azure_ttp(file_path):
    print(f"\n[+] Executing Azure TTP: {file_path}")
    try:
        with open(file_path, 'r') as file:
            ttp = yaml.safe_load(file)

        for step in ttp.get("steps", []):
            description = step.get("description", "No description provided.")
            command = step.get("action", "")
            print(f"\n[*] Step: {description}")
            print(f"[>] Command: {command}")

            try:
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"[!] Command failed: {e}")

    except FileNotFoundError:
        print(f"[!] TTP file not found: {file_path}")
    except yaml.YAMLError as e:
        print(f"[!] YAML parsing error: {e}")