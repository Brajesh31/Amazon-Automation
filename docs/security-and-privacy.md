# 🔐 Security and Privacy

## Scope

The project drives a browser to a public shopping website. A browser may expose account sessions, browsing history, regional preferences and other private state if launched with a personal profile.

## Data currently handled

The current code starts a Chrome session, deletes session cookies, and submits a product search string to a public site. It does not intentionally store product, cart or order data in an application database.

Browser diagnostics can still contain personal information. Screenshots, URLs, page source, browser logs and profile directories should be treated as potentially sensitive.

## Required safe-use practices

1. Use only systems and workflows you are authorized to test.
2. Prefer local mock pages or an approved sandbox.
3. Use a disposable browser profile, never a daily-use personal profile.
4. Do not automate sign-in, MFA, CAPTCHA solving, checkout, payment or purchases.
5. Do not bypass rate limits, anti-bot controls, fraud safeguards or access restrictions.
6. Do not store cookies, passwords, payment data or personal data in Git.
7. Redact machine paths, identifiers and tokens from logs and support reports.
8. Keep Python, Selenium, Chrome and driver components updated.

## Secrets

The current application has no required secret. `.env.example` is informational and is not loaded by the program. Never add real credentials to source files, sample configuration, issue reports or commit messages.

## Browser profile hygiene

Browser profiles can retain cookies and local storage. Use a fresh temporary profile for authorized tests and remove it when complete. Do not upload profiles as CI artifacts.

## Vulnerability reporting

Follow [SECURITY.md](../SECURITY.md) and report suspected issues privately. Do not put working secrets or personal data into a public issue.

## Responsible-use boundary

This project is not intended to evade website restrictions or automate purchasing. When the target blocks or challenges browser automation, stop. Do not attempt to disguise the browser or circumvent the control.
