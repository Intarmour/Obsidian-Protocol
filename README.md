> ⚡ Obsidian Protocol is now 100% open-source – no premium version, no paywalls.  
> Built for the community, maintained by Intarmour.

# 🌩️ Obsidian Protocol 

**Open-Source Cloud Adversary Framework**

Obsidian Protocol allows cybersecurity teams to easily test cloud-based attack techniques aligned with the MITRE ATT&CK framework.

![Multicloud](https://img.shields.io/badge/Multicloud-Ready-brightgreen)
![Air-Gapped](https://img.shields.io/badge/Air--Gapped-Compatible-blue)
![SIEM](https://img.shields.io/badge/SIEM-Splunk%20%7C%20Sentinel-orange)
![Status](https://img.shields.io/badge/Status-MVP--Complete%20%7C%20Headless--Ready-success)
![License](https://img.shields.io/badge/License-MIT-blue)
![Security](https://img.shields.io/badge/Security-First-critical)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red)
![Contributions welcome](https://img.shields.io/badge/Contributions-Welcome-ff69b4)


## 🔥 Features

- ✅ 25 **Advanced TTPs** per ogni cloud provider (AWS, Azure, GCP, Oracle, Alibaba)
- 🎯 Full scenario execution with YAML
- 🌍 **Multicloud**: AWS, Azure, GCP, Oracle, Alibaba
- 📁 **Modular CLI** with `--file`, `--provider`, `--type`
- 🧪 Auto-configurable YAML inputs via Jinja-like prompts
- 📓 **Execution logging** to `execution_log.csv`
- 🏢 Optional **AWS Organizations** cross-account support
- 🧩 SIEM integrations (Splunk, Sentinel) – *coming soon*
- 🛡️ Air-gapped environments – *experimental*
- 📦 Headless & interactive modes
- 🧠 Integrated SIEM modules with real detection content (Splunk & Sentinel)
- 🧾 CSV and JSON execution logs with structured reporting

---

## 📂 Project Structure

```
.
├── cli.py                # Main CLI interface
├── executor.py           # Executes TTPs and scenarios
├── ttps/                 # YAML-based atomic techniques
├── scenarios/            # Complex multistep simulations
├── providers/            # Provider-specific modules
│   ├── aws.py
│   ├── azure.py
│   ├── gcp.py
│   ├── oracle.py
│   └── alibaba.py
├── integrations/         # SIEM integrations (Splunk, Sentinel)
├── logs/                 # CSV/JSON logs from executions
├── tests/                # Unit tests per provider
├── .env.example          # Sample credentials
└── execution_log.csv     # Execution history
```

---

## 🚀 Quick Start

```bash
# Install requirements
pip install -r requirements.txt

# Optional: configure log format or SIEM integration in config.yaml

# Set your credentials in .env

# Run a TTP
python cli.py --file=ttps/example_ttp.yaml --type=TTP

# Run a Scenario
python cli.py --file=scenarios/example_scenario.yaml --type=Scenario
```

---


## 🔐 .env Example

```env
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AZURE_CLIENT_ID=...
AZURE_TENANT_ID=...
GOOGLE_APPLICATION_CREDENTIALS=...
ORACLE_TENANCY_ID=...
ORACLE_USER_ID=...
ALIBABA_ACCESS_KEY_ID=...
ALIBABA_ACCESS_KEY_SECRET=...
```


## 📡 SIEM Integrations

Real-world integration examples are provided under the `/integrations` folder:

- `splunk/`: SPL queries, field extractions, dashboards
- `sentinel/`: Workbooks, KQL parsers, playbooks

These modules allow you to correlate TTP and scenario activity with your SIEM pipelines, including dashboards, alerts, and response playbooks.


## Support & Contributions

Obsidian Protocol is fully open source and maintained by Intarmour.  
For enterprise support, training, or to contribute with advanced TTPs, contact us at 📧 [info@intarmour.com](mailto:info@intarmour.com).

## 🐞 Report Bugs
Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md).

## 📄 License
[MIT License](LICENSE)
