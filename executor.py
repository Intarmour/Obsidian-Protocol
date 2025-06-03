import os
import importlib
import sys
import argparse
import logging
import splunklib.client as splunk_client
import splunklib.results as splunk_results
from azure.loganalytics import LogAnalyticsDataClient
from azure.identity import DefaultAzureCredential
from azure.loganalytics.models import QueryBody

logging.basicConfig(filename='execution.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def detect_provider():
    for provider in ["AWS", "AZURE", "GCP", "ORACLE", "ALIBABA"]:
        if os.getenv(f"{provider}_ACCESS_KEY_ID") or os.getenv(f"{provider}_CREDENTIALS"):
            return provider
    return "AWS"  # Default fallback

def main():
    parser = argparse.ArgumentParser(description="Obsidian Protocol Executor")
    parser.add_argument("--file", required=True, help="Path to the TTP (ttps/) or Scenario (scenarios/) YAML file")
    parser.add_argument("--mode", choices=["ttp", "scenario"], default="ttp", help="Execution mode: ttp or scenario")
    parser.add_argument("--log-siem", action="store_true", help="Enable logging to SIEM (Splunk or Sentinel)")
    args = parser.parse_args()

    provider = detect_provider().lower()
    print(f"Detected cloud provider: {provider.upper()}")

    try:
        module = importlib.import_module(f"providers.{provider}")
        if args.mode == "ttp" and hasattr(module, "run_ttp"):
            logging.info(f"Executing TTP from ttps/{args.file} on {provider.upper()}")
            module.run_ttp(args.file)
            if args.log_siem:
                with open(args.file, 'r') as f:
                    content = f.read()
                log_to_splunk(content)
                log_to_sentinel(os.getenv("AZURE_WORKSPACE_ID"), f"CustomEvents | where RawData contains '{args.file}'")
        elif args.mode == "scenario" and hasattr(module, "run_scenario"):
            logging.info(f"Executing Scenario from scenarios/{args.file} on {provider.upper()}")
            module.run_scenario(args.file)
            if args.log_siem:
                with open(args.file, 'r') as f:
                    content = f.read()
                log_to_splunk(content)
                log_to_sentinel(os.getenv("AZURE_WORKSPACE_ID"), f"CustomEvents | where RawData contains '{args.file}'")
        else:
            logging.error(f"The module for {provider.upper()} does not implement the required method '{'run_ttp' if args.mode == 'ttp' else 'run_scenario'}'")
            print(f"[ERROR] The module for {provider.upper()} does not implement the required method '{'run_ttp' if args.mode == 'ttp' else 'run_scenario'}'")
    except ModuleNotFoundError:
        print(f"No implementation found for provider: {provider.upper()}")

    print("Execution complete. Check execution.log for more details.")

    # Placeholder for future SIEM integrations
    # For example: log_to_splunk(), log_to_sentinel()

if __name__ == "__main__":
    main()


import json

# Splunk HEC logging integration
def log_to_splunk(event_data):
    import requests

    splunk_url = os.getenv("SPLUNK_HEC_URL")
    splunk_token = os.getenv("SPLUNK_HEC_TOKEN")
    splunk_index = os.getenv("SPLUNK_INDEX", "main")

    if not splunk_url or not splunk_token:
        logging.error("Splunk HEC URL or Token not set in environment variables.")
        return

    headers = {
        "Authorization": f"Splunk {splunk_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "event": event_data,
        "sourcetype": "_json",
        "index": splunk_index
    }

    try:
        response = requests.post(splunk_url, headers=headers, data=json.dumps(payload), verify=False)
        response.raise_for_status()
        logging.info("Event successfully sent to Splunk.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send event to Splunk: {e}")

# Microsoft Sentinel logging/query integration
def log_to_sentinel(workspace_id, query):
    if not workspace_id:
        logging.error("Azure Sentinel Workspace ID not provided.")
        return

    try:
        credential = DefaultAzureCredential()
        client = LogAnalyticsDataClient(credential)
        response = client.query(workspace_id, QueryBody(query=query))
        logging.info("Sentinel query executed successfully.")
        print(response.tables)
    except Exception as e:
        logging.error(f"Failed to execute Sentinel query: {e}")