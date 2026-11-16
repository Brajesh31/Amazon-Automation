# 💻 Installation Guide

## Prerequisites

- Python 3.10 or newer.
- Git.
- Google Chrome.
- Selenium and a compatible driver setup.
- Authorization for the browser workflow and target environment.

This repository does not publish a tested OS matrix. Chrome and ChromeDriver compatibility is version-sensitive.

## Clone

```bash
git clone https://github.com/Brajesh31/Amazon-Automation.git
cd Amazon-Automation
```

## Create a virtual environment

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.venv\\Scripts\\Activate.ps1
```

Activate on Windows Command Prompt:

```bat
.venv\\Scripts\\activate.bat
```

Activate on macOS or Linux:

```bash
source .venv/bin/activate
```

If shell policy prevents activation, use the interpreter under the virtual environment directly. Do not weaken system-wide execution policy simply to run this project.

## Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Install Chrome and verify

Install Chrome separately through a trusted distribution channel. Confirm it opens. The repository's `Drivers/chromedriver` file is platform-specific and may not match the installed browser.

The current script stores a driver path but does not pass that path to `ChromeService`. Prefer Selenium Manager with a current Selenium installation, or explicitly configure a compatible driver. See [Browser and driver management](browser-and-driver.md).

## Verify environment

```bash
python --version
python -m pip show selenium
python -m pip check
python -m py_compile main.py
```

These checks validate the local Python environment and syntax. They do not validate selectors against the current live website.

## Run

```bash
python main.py
```

Review [Workflow](workflow.md) and [Security and privacy](security-and-privacy.md) first. The current script visits a live website and should not be run with a personal shopping or payment account.

## Remove local environment

Deactivate the virtual environment and delete the local `.venv` folder. The project does not install a system service or background daemon.
