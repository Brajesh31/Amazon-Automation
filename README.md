# Amazon Cart Automation

A compact Python and Selenium browser-automation proof of concept. The current script opens Amazon.com, searches for a configured product name, opens a search result, and attempts to interact with a product-page control.

> **Important:** this is an educational prototype, not a supported shopping bot or reliable end-to-end cart test. The current selector targets `wishListMainButton`, which does not establish that an item is added to the cart. Do not use this project to bypass authentication, CAPTCHAs, rate limits, fraud controls, or purchase safeguards.

## Contents

- [Project status](#project-status)
- [Current behavior](#current-behavior)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Run locally](#run-locally)
- [Safety](#safety)
- [Known limitations](#known-limitations)
- [Validation](#validation)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Project status

| Area | Current state |
|---|---|
| Language | Python |
| Browser automation | Selenium WebDriver |
| Browser | Google Chrome |
| Entry point | `main.py` |
| Structure | One Python module and one automation class |
| Configuration | Search term and target embedded in source |
| Persistence | None |
| Database | None |
| HTTP API | None |
| Automated behavior tests | Not present |
| CI | Syntax, dependency and documentation checks |
| Production readiness | Not production-ready |

## Current behavior

The `AmazonCartAutomation` class currently:

1. Constructs a Chrome WebDriver session.
2. Deletes cookies from that session.
3. Maximizes the window.
4. Opens `https://www.amazon.com/`.
5. Locates the search field by ID `twotabsearchtextbox`.
6. Searches for `Wireless Earbuds`.
7. Opens a result using a hard-coded absolute XPath.
8. Clicks an element whose ID is `wishListMainButton`.
9. Quits Chrome on the normal execution path.

The final interaction is not a verified add-to-cart operation. The selector name appears wishlist-related, and the code does not assert that cart state changed. Treat it as an unverified product-page interaction.

## Architecture

```text
Amazon-Automation/
├── main.py
├── Drivers/
│   └── chromedriver
├── docs/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── requirements.txt
├── .env.example
└── README.md
```

The project has no application server, database, frontend, scheduler, persistent data store, or service layer. The browser and external page DOM are the integration boundary.

## Requirements

- Python 3.10 or newer.
- Google Chrome.
- Selenium from `requirements.txt`.
- A compatible ChromeDriver or Selenium Manager support.
- An environment and workflow you are authorized to test.

The repository contains a platform-specific ChromeDriver binary. It may not match your operating system or Chrome version. The current code also stores a machine-specific path but does not pass it into `ChromeService`. See [Browser and driver management](docs/browser-and-driver.md).

## Installation

```bash
git clone https://github.com/Brajesh31/Amazon-Automation.git
cd Amazon-Automation
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.venv\\Scripts\\Activate.ps1
```

```bat
:: Windows Command Prompt
.venv\\Scripts\\activate.bat
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Install Chrome separately and review the driver setup before execution.

## Configuration

The current program does not load environment variables or a configuration file. The product name and target URL are hard-coded. `.env.example` is informational only.

Never put credentials, session cookies, browser profiles, payment information, or personal data in source files or examples.

## Run locally

```bash
python main.py
```

This launches a visible browser and contacts a live external website. Do not use a personal shopping or payment account. Prefer local mock pages for development and tests.

## Safety

Use only systems and workflows for which you have explicit authorization. Follow the target website's terms and applicable law. Do not automate authentication, MFA, CAPTCHA solving, checkout, payment, bulk purchasing, or bypasses of anti-bot systems and rate limits. Stop when the site blocks or challenges automation.

Read [SECURITY.md](SECURITY.md) and [Security and privacy](docs/security-and-privacy.md).

## Known limitations

1. Driver path is a developer-specific absolute path.
2. The stored path is not passed to the `ChromeService` constructor.
3. A large, platform-specific ChromeDriver binary is committed.
4. The absolute XPath is brittle and DOM-dependent.
5. The final `wishListMainButton` click is not verified as a cart action.
6. Target URL and search phrase are hard-coded.
7. Browser cleanup is not protected by `finally`.
8. There is no automated behavior test suite or mock page.
9. Live markup, localization, consent, login, and anti-automation controls can affect execution.
10. There is no structured error model or diagnostics policy.

These are current constraints, not supported features.

## Validation

```bash
python -m py_compile main.py
python -m pip check
```

CI validates syntax and repository files. It does not access Amazon or prove that live selectors work.

## Documentation

| Guide | Description |
|---|---|
| [Docs index](docs/README.md) | Full documentation navigation |
| [Architecture](docs/architecture.md) | Components and execution boundaries |
| [Installation](docs/installation.md) | Environment setup |
| [Development](docs/development.md) | Local workflow and standards |
| [Browser and driver](docs/browser-and-driver.md) | Chrome and Selenium setup |
| [Configuration](docs/configuration.md) | Current and proposed settings |
| [Workflow](docs/workflow.md) | Actual browser interaction sequence |
| [Python interface](docs/api.md) | Class methods, no HTTP API |
| [Testing](docs/testing.md) | Static and mock-based testing |
| [Security and privacy](docs/security-and-privacy.md) | Safe-use and data handling |
| [Deployment](docs/deployment.md) | Local and CI execution |
| [Operations](docs/operations.md) | Runbook and cleanup |
| [Limitations](docs/limitations.md) | Known gaps |
| [FAQ](docs/faq.md) | Common questions |
| [Database](docs/database.md) | No persistence layer |
| [Troubleshooting](docs/troubleshooting.md) | Common failures |

Maintainer guidance: [Contributing](CONTRIBUTING.md), [Code of Conduct](CODE_OF_CONDUCT.md), [Security](SECURITY.md), [Support](SUPPORT.md), [Changelog](CHANGELOG.md), and [Roadmap](ROADMAP.md).

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Keep changes safe, narrowly scoped, tested with mock pages or explicitly authorized systems, and documented accurately.

## License

MIT License. Copyright © 2025 Brajesh Kumar. See [LICENSE](LICENSE).
