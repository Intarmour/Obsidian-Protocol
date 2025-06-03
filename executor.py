import os
import importlib
import sys
import argparse
import logging

logging.basicConfig(filename='execution.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def detect_provider():
    for provider in ["AWS", "AZURE", "GCP", "ORACLE", "ALIBABA"]:
        if os.getenv(f"{provider}_ACCESS_KEY_ID") or os.getenv(f"{provider}_CREDENTIALS"):
            return provider
    return "AWS"  # Default fallback

def main():
    parser = argparse.ArgumentParser(description="Obsidian Protocol Executor")
    parser.add_argument("--file", required=True, help="Path to the TTP or Scenario YAML file")
    parser.add_argument("--mode", choices=["ttp", "scenario"], default="ttp", help="Execution mode: ttp or scenario")
    args = parser.parse_args()

    provider = detect_provider().lower()
    print(f"Detected cloud provider: {provider.upper()}")

    try:
        module = importlib.import_module(f"providers.{provider}")
        if args.mode == "ttp" and hasattr(module, "run_ttp"):
            logging.info(f"Executing TTP from {args.file} on {provider.upper()}")
            module.run_ttp(args.file)
        elif args.mode == "scenario" and hasattr(module, "run_scenario"):
            logging.info(f"Executing Scenario from {args.file} on {provider.upper()}")
            module.run_scenario(args.file)
        else:
            logging.error(f"The module for {provider.upper()} does not implement the required method for mode {args.mode}")
            print(f"The module for {provider.upper()} does not implement the required method for mode {args.mode}")
    except ModuleNotFoundError:
        print(f"No implementation found for provider: {provider.upper()}")

    print("Execution complete. Check execution.log for more details.")

if __name__ == "__main__":
    main()