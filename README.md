# 🌩️ Obsidian Protocol

**Open-Source Cloud Adversary Simulation Framework**

Obsidian Protocol allows cybersecurity teams to easily simulate realistic cloud-based attack techniques aligned with the MITRE ATT&CK framework.

![Multicloud](https://img.shields.io/badge/Multicloud-Ready-brightgreen)
![Air-Gapped](https://img.shields.io/badge/Air--Gapped-Compatible-blue)
![SIEM](https://img.shields.io/badge/SIEM-Splunk%20%7C%20Sentinel-orange)
![Status](https://img.shields.io/badge/Status-MVP--Complete-success)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

## 🔓 Free Edition Includes
- 10 advanced AWS TTPs (MITRE ATT&CK aligned)
- 5 realistic multi-phase attack scenarios
- Interactive CLI with guided selection and job logging
- `.env` based credential injection
- Air-gapped compatible
- MIT License

## 🚀 Quick Installation Guide

### Clone the repo
```bash
git clone https://github.com/intarmour/obsidian-protocol.git
cd obsidian-protocol
```

### Setup Python environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configure your environment
```bash
cp .env.example .env
nano .env
```


### Run CLI
```bash
python cli.py
```

### Using the CLI (Interactive Mode)
Once you run the CLI, you’ll be guided through:

1. Selecting your cloud provider (currently only AWS is available in the Free Edition)
2. Verifying your API credentials from the `.env` file
3. Choosing between running individual TTPs or full scenarios
4. Executing the selected adversary technique with live feedback

All executions are logged and stored per job ID for easy auditing and traceability.

## 🛠️ Premium Version
Interested in additional functionality?
- 50+ comprehensive TTPs (AWS, Azure, GCP, Oracle, Alibaba)
- SIEM integration (Splunk & Sentinel)
- Air-gapped support
- Priority support and advanced reporting

📧 [info@intarmour.com](mailto:info@intarmour.com)

## 🐞 Report Bugs
Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md).

## 📄 License
[MIT License](LICENSE)
