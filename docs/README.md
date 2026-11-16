# Documentation Index

This directory contains the technical and operational documentation for Amazon Cart Automation. The guides describe the repository as it exists today, including limitations and unimplemented capabilities. They do not imply that the prototype is a production-ready shopping automation tool.

## Start here

1. Read the root [README](../README.md) for project scope, setup, and current behavior.
2. Read [Installation](installation.md) before running the script.
3. Review [Browser and driver management](browser-and-driver.md) because the checked-in driver configuration is not portable.
4. Read [Security and privacy](security-and-privacy.md) before any live browser interaction.
5. Use [Testing strategy](testing.md) to validate changes without interacting with a real shopping account.

## Technical guides

| Guide | Coverage |
|---|---|
| [Architecture](architecture.md) | Components, runtime boundaries, execution sequence |
| [Workflow](workflow.md) | Current browser journey and selector assumptions |
| [API](api.md) | Local class methods and behavior |
| [Configuration](configuration.md) | Hard-coded values, environment and future configuration |
| [Browser and driver management](browser-and-driver.md) | Selenium Manager, Chrome, ChromeDriver |
| [Database](database.md) | Current lack of persistence and database |
| [Development](development.md) | Coding workflow, validation, proposed structure |
| [Installation](installation.md) | Python environment and dependencies |
| [Testing](testing.md) | Static checks, mock fixtures, authorized tests |
| [Limitations](limitations.md) | Known implementation gaps |

## Operations and quality

| Guide | Coverage |
|---|---|
| [Security and privacy](security-and-privacy.md) | Data minimization, browser profiles, responsible use |
| [Deployment](deployment.md) | Controlled local/CI execution |
| [Operations](operations.md) | Runbook, cleanup, incident handling |
| [Troubleshooting](troubleshooting.md) | Driver, browser, selector and dependency failures |
| [FAQ](faq.md) | Frequently asked questions |

## Maintainer documents

- [Contributing](../CONTRIBUTING.md)
- [Code of Conduct](../CODE_OF_CONDUCT.md)
- [Security Policy](../SECURITY.md)
- [Support](../SUPPORT.md)
- [Changelog](../CHANGELOG.md)
- [Roadmap](../ROADMAP.md)
- [Citation metadata](../CITATION.cff)

## Scope discipline

The project currently has one Python script and no server, API, database, scheduler, user interface, or test suite. Documentation for these absent systems explicitly says they are absent. Any future addition should update the architecture, workflow, tests, security guidance, README, and changelog in the same change.
