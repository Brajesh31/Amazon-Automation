# Documentation Index

These guides describe the repository as it exists today. They distinguish working behavior from assumptions and future proposals.

## Start here

1. [Root README](../README.md), project scope and setup.
2. [Installation](installation.md), local environment.
3. [Browser and driver management](browser-and-driver.md), portability and Selenium Manager.
4. [Security and privacy](security-and-privacy.md), safe browser execution.
5. [Testing](testing.md), validation without live shopping actions.

## Technical guides

| Guide | Coverage |
|---|---|
| [Architecture](architecture.md) | Runtime components and boundaries |
| [Workflow](workflow.md) | Exact current browser sequence |
| [API](api.md) | Local Python class interface, not HTTP |
| [Configuration](configuration.md) | Hard-coded values and future settings |
| [Browser and driver](browser-and-driver.md) | Selenium, Chrome and driver management |
| [Database](database.md) | Current lack of persistence |
| [Development](development.md) | Coding and dependency standards |
| [Installation](installation.md) | Environment setup |
| [Testing](testing.md) | Static checks, mocks and authorized tests |
| [Limitations](limitations.md) | Implementation gaps |

## Operations and quality

| Guide | Coverage |
|---|---|
| [Security and privacy](security-and-privacy.md) | Data minimization and responsible use |
| [Deployment](deployment.md) | Controlled local and CI execution |
| [Operations](operations.md) | Runbook, cleanup and incidents |
| [Troubleshooting](troubleshooting.md) | Browser, driver and selector failures |
| [FAQ](faq.md) | Common project questions |

## Maintainer documents

- [Contributing](../CONTRIBUTING.md)
- [Code of Conduct](../CODE_OF_CONDUCT.md)
- [Security policy](../SECURITY.md)
- [Support](../SUPPORT.md)
- [Changelog](../CHANGELOG.md)
- [Roadmap](../ROADMAP.md)
- [Citation metadata](../CITATION.cff)

## Scope discipline

The project currently has one Python script and no server, database, scheduler, frontend or test suite. Documents for absent components explicitly state that they do not exist. New capabilities should be documented and tested in the same change.
