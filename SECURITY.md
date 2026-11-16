# Security Policy

## Project scope

This repository is a small educational Selenium prototype. It is not designed for production shopping, account automation, checkout or payment handling.

## Safe operation

- Use only systems and workflows you have explicit permission to test.
- Prefer local mock pages or an approved sandbox.
- Do not automate sign-in, MFA, CAPTCHA solving, checkout, payment or purchases.
- Do not bypass rate limits, bot detection, fraud controls or other access safeguards.
- Do not store cookies, session tokens, passwords, payment data or personal information in Git.
- Keep Python, Selenium, Chrome and driver components updated.
- Redact machine-specific paths, identifiers, tokens and personal data from reports.

## Reporting vulnerabilities

Report suspected security issues privately to the repository maintainer, Brajesh Kumar, through [@brajesh31](https://github.com/Brajesh31). Do not publish exploit details, working credentials or personal data in a public issue.

Include a concise description, affected component, impact, sanitized reproduction steps and a suggested mitigation where possible. Allow reasonable time for investigation and remediation before public disclosure.

## Secret exposure

If a credential or session token is committed, revoke or rotate it immediately. Removing it from the latest commit does not invalidate the secret or remove it from repository history.
