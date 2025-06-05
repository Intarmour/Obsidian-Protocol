> ⚡ Obsidian Protocol is now 100% open-source – no premium version, no paywalls.  
> Built for the community, maintained by Intarmour.

# 🌩️ Obsidian Protocol 

**Open-Source Cloud Adversary Framework**

Obsidian Protocol allows cybersecurity teams to easily test cloud-based attack techniques aligned with the MITRE ATT&CK framework.

![Multicloud](https://img.shields.io/badge/Multicloud-Ready-brightgreen)
![SIEM](https://img.shields.io/badge/SIEM-Splunk%20%7C%20Sentinel-orange)
![License](https://img.shields.io/badge/License-MIT-blue)
![Status](https://img.shields.io/badge/Status-Open--Source-success)
![CI](https://github.com/Intarmour/Obsidian-Protocol/actions/workflows/python-tests.yml/badge.svg)


## 🔥 Features

- ✅ 25+ advanced TTPs for each major cloud provider: AWS, Azure, GCP, Oracle, Alibaba
- 🎯 Full scenario execution with YAML and headless CLI support
- 🧩 Native SIEM integrations (Splunk & Sentinel) for real-time correlation
- 🛡️ Air-gapped and enterprise-ready (no internet dependency)
- 📁 Modular multicloud CLI: --file, --provider, --type
- ⚙️ Dynamic config management via config.yaml
- 📓 Structured CSV/JSON logs for analytics and compliance
- 🌐 Optional AWS Organizations support for cross-account testing
- 🧪 Auto-templated YAML via Jinja-like variable injection

---

## 📂 Project Structure

```
├── config.yaml          # Global configuration for providers and logging
├── cli.py               # Main CLI interface
├── executor.py          # Core execution engine
├── ttps/                # Atomic TTPs in YAML format
├── scenarios/           # Multistep scenario executions
├── providers/           # Multicloud provider modules
│   ├── aws.py
│   ├── azure.py
│   ├── gcp.py
│   ├── oracle.py
│   └── alibaba.py
├── integrations/        # SIEM integrations: Splunk & Sentinel
│   ├── splunk/
│   └── sentinel/
├── logs/                # Execution logs and reports
├── tests/               # Unit tests per provider
├── .env.example         # Example environment credentials
└── execution_log.csv    # Execution audit log
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
