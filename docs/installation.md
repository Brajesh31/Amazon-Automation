# Installation Guide

## 1. Supported baseline

The repository currently targets Python 3.10 or newer and uses Selenium. The project does not currently publish a tested operating-system matrix. Chrome and its driver must be compatible with each other.

## 2. Prerequisites

Install:

- Python 3.10+.
- Google Chrome.
- Git.
- A terminal with permission to create a virtual environment.
- Network access for installing dependencies and, if Selenium Manager is used, retrieving an appropriate driver.

For repeatable work, record the exact Python, Selenium, Chrome, and ChromeDriver versions used during validation.

## 3. Clone the repository

```bash
git clone https://github.com/Brajesh31/Amazon-Automation.git
cd Amazon-Automation
```

## 4. Create a virtual environment

```bash
python -m venv .venv
```

Activate it using the command appropriate for your shell:

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

If PowerShell blocks activation, use the Python executable in the virtual environment directly or consult your machine's execution policy. Do not weaken system policy globally just to run this project.

## 5. Install dependencies

Upgrade pip and install the repository's declared package set:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 6. Install and verify Chrome

Install Chrome through the official distribution channel for your operating system. Check that the executable starts before launching Selenium.

The repository includes a Linux ChromeDriver binary under `Drivers/`. It is not a universal driver and it may not match your browser. The current Python code does not explicitly pass its hard-coded path to `ChromeService`. Prefer Selenium Manager with a current Selenium release, or explicitly configure a locally installed compatible driver. See [Browser and driver management](browser-and-driver.md).

## 7. Verify the environment

```bash
python --version
python -m pip show selenium
python -m pip check
python -m py_compile main.py
```

These commands verify the Python installation and syntax, not whether the live website's DOM still matches the selectors.

## 8. Run

```bash
python main.py
```

The current entry point opens a live website and uses a hard-coded product search. Review [Workflow](workflow.md) and [Security and privacy](security-and-privacy.md) first. Do not use personal shopping or payment accounts.

## 9. Uninstall

Deactivate the virtual environment, then remove the local `.venv` directory. The project does not install a system service or background process.

