import os
import inquirer
import subprocess
from dotenv import load_dotenv
import yaml

print("""
===========================================
   Obsidian Protocol – Adversary Emulator
   License: MIT
   Contact: security@intarmour.com
   Description: Execute adversary TTPs and scenarios in cloud environments (AWS)
===========================================\n""")

load_dotenv()

import boto3

def test_aws_connection():
    try:
        sts = boto3.client("sts")
        sts.get_caller_identity()
        return True
    except Exception:
        return False

def load_env_credentials():
    return {
        "AWS_ACCESS_KEY_ID": os.getenv("AWS_ACCESS_KEY_ID", ""),
        "AWS_SECRET_ACCESS_KEY": os.getenv("AWS_SECRET_ACCESS_KEY", ""),
        "AWS_REGION": os.getenv("AWS_REGION", "us-east-1")
    }

def select_provider():
    providers = ["AWS (Free Version)"]
    questions = [
        inquirer.List('provider',
                      message="Select cloud provider",
                      choices=providers)
    ]
    answers = inquirer.prompt(questions)
    return answers['provider']

def select_execution_type():
    options = ["Run TTP", "Run Scenario", "Exit"]
    questions = [
        inquirer.List('action',
                      message="What do you want to do?",
                      choices=options)
    ]
    answers = inquirer.prompt(questions)
    return answers['action']

def list_yaml_files(folder):
    if not os.path.isdir(folder):
        return []
    return [f for f in os.listdir(folder) if f.endswith(".yaml")]

def select_yaml_file(file_list, label):
    if not file_list:
        print(f"No {label} files found.")
        return None
    questions = [
        inquirer.List('selection', message=f"Select a {label} to run", choices=file_list)
    ]
    answers = inquirer.prompt(questions)
    return answers['selection']

def run_simulation(file_path, sim_type):
    print(f"\n--- Executing {sim_type}: {file_path} ---")
    try:
        subprocess.run(["python", "executor.py", f"--file={file_path}"], check=True)
    except FileNotFoundError:
        print("Error: executor.py not found. Make sure it exists in the project directory.")
    except subprocess.CalledProcessError as e:
        print(f"Execution failed: {e}")
    print(f"--- {sim_type} execution complete ---\n")
    if sim_type == "TTP":
        temp_path = os.path.join("ttps", "_temp_ttp.yaml")
        if os.path.exists(temp_path):
            os.remove(temp_path)

def configure_ttp(filepath):
    def recursive_replace(data, params):
        if isinstance(data, dict):
            return {k: recursive_replace(v, params) for k, v in data.items()}
        elif isinstance(data, list):
            return [recursive_replace(item, params) for item in data]
        elif isinstance(data, str) and "{{" in data and "}}" in data:
            param_name = data.strip("{{}}").strip()
            if param_name not in params:
                user_input = input(f"Enter value for '{param_name}': ").strip()
                params[param_name] = user_input
            return params[param_name]
        else:
            return data

    with open(filepath, 'r') as f:
        ttp_data = yaml.safe_load(f)

    params = {}
    configured_data = recursive_replace(ttp_data, params)

    temp_file = os.path.join("ttps", "_temp_ttp.yaml")
    with open(temp_file, 'w') as f:
        yaml.dump(configured_data, f)
    return temp_file

def main():
    print("Welcome to Obsidian Protocol - CLI Mode\n")

    creds = load_env_credentials()
    if not creds["AWS_ACCESS_KEY_ID"] or not creds["AWS_SECRET_ACCESS_KEY"]:
        print("Missing AWS credentials in .env file. Please create a .env file with the required keys:")
        print("AWS_ACCESS_KEY_ID=your_access_key")
        print("AWS_SECRET_ACCESS_KEY=your_secret_key")
        print("AWS_REGION=your_region (default: us-east-1)")
        return

    print("Detected AWS credentials:")
    print(f"- AWS_ACCESS_KEY_ID: {creds['AWS_ACCESS_KEY_ID'][:4]}***")
    print(f"- AWS_REGION: {creds['AWS_REGION']}\n")

    if not test_aws_connection():
        print("❌ AWS credentials appear to be invalid or unauthorized. Please verify them.")
        return

    provider = select_provider()
    print(f"Selected Provider: {provider}\n")

    while True:
        action = select_execution_type()
        if action == "Exit":
            print("Goodbye.")
            break
        elif action == "Run TTP":
            ttps = list_yaml_files("ttps")
            selected_ttp = select_yaml_file(ttps, "TTP")
            if selected_ttp:
                # Parameters for TTPs will be requested from the user during execution
                confirm = input(f"Run TTP {selected_ttp}? [Y/n]: ").strip().lower()
                if confirm in ["y", ""]:
                    configured_ttp_path = configure_ttp(os.path.join("ttps", selected_ttp))
                    run_simulation(configured_ttp_path, "TTP")
        elif action == "Run Scenario":
            scenarios = list_yaml_files("scenarios")
            selected_scenario = select_yaml_file(scenarios, "Scenario")
            if selected_scenario:
                confirm = input(f"Run Scenario {selected_scenario}? [Y/n]: ").strip().lower()
                if confirm in ["y", ""]:
                    run_simulation(os.path.join("scenarios", selected_scenario), "Scenario")

if __name__ == "__main__":
    main()