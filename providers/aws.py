import subprocess
import yaml
import os

def execute_aws_ttp(filepath):
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)

        print(f"\n[+] TTP: {data.get('name')}")
        print(f"[-] Description: {data.get('description')}")
        print(f"[-] MITRE Technique: {data.get('mitre_technique')}")
        print(f"[-] Stage: {data.get('stage')}\n")

        for step in data.get('steps', []):
            action = step.get('action')
            description = step.get('description')
            print(f"[>] {description}")
            print(f"    Command: {action}")
            try:
                subprocess.run(action, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"[!] Command failed: {e}")
            print()
    except Exception as e:
        print(f"[!] Failed to execute TTP: {e}")