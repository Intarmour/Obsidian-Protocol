import subprocess
import yaml

def execute_alibaba_ttp(file_path):
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