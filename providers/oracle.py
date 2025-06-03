

import subprocess

def execute_oracle_command(command, description=""):
    print(f"\n[Oracle] {description}")
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        print(result.stdout)
        if result.stderr:
            print("[stderr]", result.stderr)
    except Exception as e:
        print(f"Error executing command: {e}")

def run_ttp(steps):
    for step in steps:
        action = step.get("action", "")
        description = step.get("description", "No description")
        if action:
            execute_oracle_command(action, description)