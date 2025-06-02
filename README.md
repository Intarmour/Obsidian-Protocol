# 🌩️ Obsidian Protocol 

**Open-Source Cloud Adversary Framework**

Obsidian Protocol allows cybersecurity teams to easily test cloud-based attack techniques aligned with the MITRE ATT&CK framework.

![Multicloud](https://img.shields.io/badge/Multicloud-Ready-brightgreen)
![Air-Gapped](https://img.shields.io/badge/Air--Gapped-Compatible-blue)
![SIEM](https://img.shields.io/badge/SIEM-Splunk%20%7C%20Sentinel-orange)
![Status](https://img.shields.io/badge/Status-MVP--Complete-success)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)
![Maintenance](https://img.shields.io/badge/Maintained-yes-brightgreen)
![Contributions welcome](https://img.shields.io/badge/Contributions-Welcome-ff69b4)
![Last Commit](https://img.shields.io/github/last-commit/intarmour/obsidian-protocol)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
![Framework](https://img.shields.io/badge/Built%20With-Python%20%7C%20Boto3%20%7C%20YAML-blue)
![Security](https://img.shields.io/badge/Security-First-critical)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red)
![Issues](https://img.shields.io/github/issues/intarmour/obsidian-protocol)

## Free Edition Includes
- 10 advanced AWS TTPs (MITRE ATT&CK aligned)
- 5 realistic multi-phase attack scenarios
- Interactive CLI with guided selection and job logging
- `.env` based credential injection
- Air-gapped compatible
- MIT License

## Quick Installation Guide

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

When starting the CLI, a banner with project info, license, and contact will be shown. This helps ensure clear attribution and communication in lab environments.

### Using the CLI (Interactive Mode)
Once you run the CLI, you’ll be guided through:

1. Selecting your cloud provider (currently only AWS is available in the Free Edition)
2. Verifying your API credentials from the `.env` file
3. Choosing between running individual TTPs or full scenarios
4. Executing the selected adversary technique with live feedback

All executions are logged and stored per job ID for easy auditing and traceability.

## Premium Version
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
