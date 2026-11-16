# Deployment and Execution

## Deployment model

This repository is a local Python script, not a web application or service. It has no server, database, queue, scheduler or deployment manifest.

The recommended development environment is an isolated virtual environment and a disposable browser profile.

## CI execution

GitHub Actions performs repository checks and Python syntax validation. It does not start a browser or access Amazon. This keeps CI independent of live third-party page markup and avoids unapproved shopping actions.

If browser testing is added later, use a local mock site, controlled test data and pinned browser tooling. Ensure the browser is closed after the test.

## Machine preparation

1. Install Python.
2. Install Chrome only when browser checks are needed.
3. Create an isolated virtual environment.
4. Install requirements.
5. Run static checks.
6. Use a local mock or explicitly approved target for behavior testing.
7. Remove disposable profiles and sanitized test artifacts after the run.

## Scheduling

Do not schedule unattended shopping activity. Any future scheduled job must have a narrow authorized testing purpose, bounded runtime, execution limits and a documented stop condition.

## Secrets and artifacts

The current application requires no secret. If future controlled test infrastructure requires a sandbox credential, store it in the platform secret manager and use least privilege. Do not upload cookies, user profiles, payment data or unredacted screenshots as build artifacts.

## Rollback

There is no deployed service to roll back. Revert the relevant commit and reinstall a known compatible Python dependency and browser set. Record browser and driver versions to reproduce compatibility issues.
