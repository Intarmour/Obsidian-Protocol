# Security Policy

## Scope

This security policy applies to all source code, configuration files, infrastructure scripts, and documentation contained in the [Obsidian Protocol](https://github.com/Intarmour/Obsidian-Protocol) repository.

## Threat Model

The Obsidian Protocol is a multicloud adversary simulation framework and assumes potential abuse by actors capable of exploiting cloud APIs, misconfigured permissions, and infrastructure vulnerabilities. We are primarily concerned with:

- Remote code execution vulnerabilities
- Privilege escalation and unauthorized access
- Sensitive data exposure
- Misuse of API keys or provider credentials
- Injection attacks against command execution

## Reporting a Vulnerability

If you discover a security vulnerability, we appreciate your help in disclosing it responsibly.

Please report it via email to [info@intarmour.com](mailto:info@intarmour.com). We will respond as quickly as possible, typically within 72 hours.

Include the following in your report:
- A detailed description of the vulnerability
- Steps to reproduce the issue
- Potential impact and affected components
- Any logs, screenshots, or proof-of-concept code
- Suggested mitigations if available

Do **not** create public GitHub issues for security-related matters.

## PGP Key

For encrypted communication, a PGP key will be published at: [https://intarmour.com/pgp.txt](https://intarmour.com/pgp.txt) (Coming Soon)

## Supported Versions

We currently support the latest stable release. Minor versions in the 1.0.x line will receive security updates for at least 6 months after release.

| Version | Supported | Notes                         |
|---------|-----------|-------------------------------|
| 1.0.x   | ✅        | Latest release line supported |
| < 1.0   | ❌        | No longer maintained           |

## Response Process

1. Vulnerability report is acknowledged within 72 hours.
2. Internal validation and risk assessment is performed.
3. A fix is developed and tested.
4. The fix is released in a patch version (e.g. 1.0.2).
5. A public disclosure is made with credit to the reporter if desired.

We may coordinate with third-party cloud vendors if the issue affects external environments.

## Disclosure Policy

We ask that you:
- Give us reasonable time to remediate the issue before disclosing it publicly.
- Do not exploit the vulnerability beyond testing.
- Avoid actions that compromise privacy, data integrity, or service availability.

## Changelog

- **2025-06-07**: Initial publication of full security policy.