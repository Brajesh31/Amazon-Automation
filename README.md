# Amazon Cart Automation

A compact Python and Selenium browser-automation proof of concept. The current script opens Amazon.com, searches for a configured product name, opens a search result, and attempts to interact with a product-page control.

> **Important scope note:** this repository is an educational prototype, not a supported shopping bot or a reliable end-to-end cart test. The current selector targets an element with ID `wishListMainButton`, which does not establish that the item is added to the cart. The automation must not be used to bypass authentication, CAPTCHAs, rate limits, fraud controls, or purchase safeguards.

## Contents

- [Project status](#project-status)
- [What the current implementation does](#what-the-current-implementation-does)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Run locally](#run-locally)
- [Safety and responsible use](#safety-and-responsible-use)
- [Known limitations](#known-limitations)
- [Validation](#validation)
- [Documentation map](#documentation-map)
- [Contributing](#contributing)
- [License](#license)

## Project status

| Area | Current state |
|---|---|
| Language | Python |
| Browser automation | Selenium WebDriver |
| Browser | Google Chrome |
| Entry point | `main.py` |
| Application structure | Single Python module and one automation class |
| Configuration | Search term is currently hard-coded in the script |
| Persistence | None |
| Database | None |
| HTTP API | None |
| Automated tests | No test suite is currently present |
| CI | Repository checks are defined in GitHub Actions |
| Production readiness | Not production-ready |

## What the current implementation does

The `AmazonCartAutomation` class in `main.py` currently performs the following sequence:

1. Constructs a Chrome WebDriver session.
2. Deletes cookies from the newly created browser session.
3. Maximizes the browser window when `setup()` is called.
4. Opens `https://www.amazon.com/`.
5. Locates the search box using `twotabsearchtextbox`.
6. Enters the hard-coded search term `Wireless Earbuds` and submits the search.
7. Waits for a first-result link using an absolute XPath and clicks it.
8. Waits for an element with ID `wishListMainButton` and clicks it.
9. Quits Chrome when `close_browser()` is called.

The final interaction is not a verified add-to-cart operation. The element identifier suggests a wishlist-related control, and Amazon page structure may vary by region, account state, experiments, and time. Treat the final action as an unverified product-page interaction until it has been redesigned and tested against an explicitly authorized test environment.

## Architecture

The implementation is intentionally small:

```text
Amazon-Automation/
├── main.py                 # Selenium workflow and entry point
├── Drivers/
│   └── chromedriver        # Committed platform-specific driver binary
├── docs/                   # Project and maintainer documentation
├── .github/
│   └── workflows/          # Repository validation workflow
├── .env.example            # Notes about current configuration
├── requirements.txt        # Python dependency declaration
└── README.md
```

There is currently no page-object layer, configuration class, API server, database, task queue, persistent cart model, or browser-independent domain layer. The browser and the external site's DOM are the primary integration boundary.

## Requirements

- Python 3.10 or newer.
- Google Chrome installed on the machine running the script.
- Selenium installed in the active Python environment.
- A compatible ChromeDriver, or Selenium Manager support in the installed Selenium version.
- An environment and target for which the operator has explicit permission to run browser automation.

Chrome and ChromeDriver compatibility is version-sensitive. Prefer Selenium Manager through a current Selenium installation rather than relying on a checked-in driver executable. See [Installation](docs/installation.md) and [Browser and driver management](docs/browser-and-driver.md).

## Installation

Clone the repository and create an isolated virtual environment:

```bash
git clone https://github.com/Brajesh31/Amazon-Automation.git
cd Amazon-Automation
python -m venv .venv
```

Activate it:

```bash
# Windows PowerShell
.venv\\Scripts\\Activate.ps1

# Windows Command Prompt
.venv\\Scripts\\activate.bat

# macOS / Linux
source .venv/bin/activate
```

Install the declared dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Install Google Chrome separately. Do not assume the committed driver binary is suitable for your operating system or installed Chrome version.

## Configuration

The current script does not read environment variables or a configuration file. Its product search term is specified in the `__main__` block. Its `chromedriver_path` value is a machine-specific absolute path, but the current `ChromeService()` constructor does not pass that path to Selenium.

For a local experiment, review the driver configuration before execution. Do not put passwords, browser cookies, session tokens, payment data, or personal account information in source files, environment examples, screenshots, or issue reports.

## Run locally

After installation and a review of the current limitations:

```bash
python main.py
```

This opens a visible browser and contacts a live external website. Do not run it against a personal shopping account or initiate checkout or payment activity. For development and repeatable validation, prefer a local mock page as described in [Testing strategy](docs/testing.md).

## Safety and responsible use

This repository is for learning Selenium and understanding browser automation. Use it only on systems and workflows you are authorized to test.

- Follow the target website's terms, policies, and applicable law.
- Do not bypass login, MFA, CAPTCHA, bot detection, rate limits, regional controls, fraud controls, or purchase confirmation safeguards.
- Do not automate checkout, payment, account creation, bulk purchasing, or inventory hoarding.
- Do not collect or store account data, cookies, personal data, or payment information.
- Use a disposable browser profile and non-sensitive test data.
- Prefer controlled mock pages or an approved sandbox.
- Stop when the site blocks or challenges automated access. Do not attempt to evade the control.

Read [SECURITY.md](SECURITY.md) before changing the automation behavior.

## Known limitations

1. **Non-portable driver path:** `main.py` contains a developer-machine path.
2. **Driver configuration mismatch:** the path is stored in an attribute and an environment variable, but the constructed `ChromeService()` does not use that attribute as its executable path.
3. **Bundled binary:** `Drivers/chromedriver` is a large, platform-specific executable and may not match the installed browser.
4. **Brittle selector:** an absolute XPath is tied to a specific DOM layout and search result arrangement.
5. **Unverified action:** `wishListMainButton` is not a reliable assertion that a cart operation occurred.
6. **Hard-coded target and data:** the site URL and search phrase are embedded in the script.
7. **Cleanup is not exception-safe:** an exception before `close_browser()` may leave the browser process running.
8. **No automated behavioral tests:** there are no current mocked page tests or browser integration tests.
9. **External-site instability:** consent pages, localization, login state, markup changes, and anti-automation controls can interrupt the flow.
10. **No observability contract:** there is no structured logging, screenshot policy, retry budget, or standardized failure report.

These are known constraints, not features. Do not treat a successful browser launch as proof that the workflow completed correctly.

## Validation

Run a syntax check:

```bash
python -m py_compile main.py
```

Run repository checks:

```bash
python -m pip check
```

The CI workflow validates Python syntax and documentation structure. It does not access Amazon, prove that the selectors still work, or make live purchases. See [Testing strategy](docs/testing.md).

## Documentation map

| Document | Purpose |
|---|---|
| [Documentation index](docs/README.md) | Complete guide to the documentation set |
| [Architecture](docs/architecture.md) | Current components, boundaries, and execution flow |
| [Installation](docs/installation.md) | Environment setup and dependencies |
| [Development](docs/development.md) | Local workflow and coding conventions |
| [Browser and driver management](docs/browser-and-driver.md) | Chrome, ChromeDriver, Selenium Manager |
| [Configuration](docs/configuration.md) | Current hard-coded configuration and future options |
| [Automation workflow](docs/workflow.md) | Step-by-step behavior and selector assumptions |
| [API](docs/api.md) | Local Python class interface, not an HTTP API |
| [Testing strategy](docs/testing.md) | Static checks, mock testing, and safe browser tests |
| [Troubleshooting](docs/troubleshooting.md) | Common local failures |
| [Security and privacy](docs/security-and-privacy.md) | Data handling and safe execution boundaries |
| [Deployment](docs/deployment.md) | Controlled execution and CI considerations |
| [Operations](docs/operations.md) | Runbooks, cleanup, and failure handling |
| [Limitations](docs/limitations.md) | Explicit technical and behavioral constraints |
| [FAQ](docs/faq.md) | Common project questions |
| [Database](docs/database.md) | Why no database is used |
| [Changelog](CHANGELOG.md) | Project changes |
| [Roadmap](ROADMAP.md) | Planned improvements |

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), follow the safety boundaries, and include evidence for any behavior change. Tests should use a local mock page or a specifically authorized environment. Do not include secrets or browser session data in a contribution.

## License

MIT License. Copyright © 2025 Brajesh Kumar. See [LICENSE](LICENSE).

Last updated: 2026-11-16 03:06 UTC
