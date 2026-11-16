# 📚 Documentation Index

Welcome to the technical documentation for **Amazon Cart Automation**. These guides describe the repository as it exists today, distinguish implemented behavior from assumptions, and record future improvement areas.

> 💡 Start with the root [README](../README.md) for the project overview and quick setup.

## 🚀 Start Here

1. 📖 [Root README](../README.md), project scope and quick start.
2. 💻 [Installation](installation.md), local Python environment.
3. 🌐 [Browser and Driver Management](browser-and-driver.md), Chrome and Selenium Manager.
4. 🔐 [Security and Privacy](security-and-privacy.md), safe browser execution.
5. 🧪 [Testing Strategy](testing.md), validation without live shopping actions.

## 🏗️ Technical Guides

| Guide | Coverage |
|---|---|
| 🏗️ [Architecture](architecture.md) | Runtime components and boundaries |
| 🔄 [Workflow](workflow.md) | Exact current browser sequence |
| 🔌 [Python Interface](api.md) | Local class methods, not an HTTP API |
| ⚙️ [Configuration](configuration.md) | Hard-coded values and future settings |
| 🌐 [Browser and Driver](browser-and-driver.md) | Selenium, Chrome and driver management |
| 🗃️ [Database](database.md) | Current lack of persistence |
| 🧑‍💻 [Development](development.md) | Coding and dependency standards |
| 💻 [Installation](installation.md) | Environment setup |
| 🧪 [Testing](testing.md) | Static checks, mocks and authorized tests |
| ⚠️ [Limitations](limitations.md) | Implementation gaps |

## 🛡️ Operations and Quality

| Guide | Coverage |
|---|---|
| 🔐 [Security and Privacy](security-and-privacy.md) | Data minimization and responsible use |
| 🚀 [Deployment](deployment.md) | Controlled local and CI execution |
| 🧰 [Operations](operations.md) | Runbook, cleanup and incidents |
| 🩺 [Troubleshooting](troubleshooting.md) | Browser, driver and selector failures |
| ❓ [FAQ](faq.md) | Common project questions |

## 🧑‍🤝‍🧑 Maintainer Documents

- 🤝 [Contributing](../CONTRIBUTING.md)
- 🧭 [Code of Conduct](../CODE_OF_CONDUCT.md)
- 🔒 [Security Policy](../SECURITY.md)
- 🆘 [Support](../SUPPORT.md)
- 📝 [Changelog](../CHANGELOG.md)
- 🗺️ [Roadmap](../ROADMAP.md)
- 📌 [Citation Metadata](../CITATION.cff)

## 🧭 Documentation Principles

- ✅ Describe implemented behavior accurately.
- 🧪 Separate verified behavior from assumptions.
- ⚠️ State limitations instead of hiding them.
- 🔐 Avoid publishing credentials, cookies or personal data.
- 🔄 Update relevant documentation when source behavior changes.

## 📎 Scope Discipline

The project currently has one Python script and no server, database, scheduler, frontend or automated behavior test suite. Documentation for absent components explicitly says they do not exist. New capabilities should be documented and tested in the same change.
