# Development Guide

## Goals

Keep this repository a small, understandable Selenium learning project. Improve reliability through explicit configuration, browser lifecycle management, stable selectors, and repeatable mock-based tests. Avoid broad automation against live shopping flows.

## Repository conventions

- Keep Python source readable and use descriptive names.
- Separate configuration from page interaction.
- Centralize selectors rather than scattering raw XPath expressions.
- Prefer explicit waits and meaningful expected conditions.
- Use `try/finally` or a context manager to ensure that browser processes close.
- Do not commit local driver binaries, secrets, browser profiles, cookies, downloads, or screenshots containing personal data.
- Document any supported Python, Selenium, Chrome, or driver version changes.

## Local development loop

1. Create and activate a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Make a narrowly scoped code change.
4. Run `python -m py_compile main.py`.
5. Run `python -m pip check`.
6. Add or update a mock-based test for behavior.
7. Review the diff for personal data, generated artifacts, and inaccurate documentation.
8. Update the README, relevant docs, and changelog when behavior changes.

## Current code boundaries

At present, `main.py` owns browser creation, navigation, element lookup, and the top-level invocation. The method called `search_and_add_to_cart` does not verify an add-to-cart result. Do not write tests that assert that it adds a product to the cart unless the implementation is first corrected and validated against a safe test fixture.

## Suggested future layout

The following is a possible future structure, not a claim about files that currently exist:

```text
src/
  amazon_automation/
    __init__.py
    config.py
    browser.py
    pages/
      search_page.py
      product_page.py
    workflow.py
tests/
  unit/
  fixtures/
```

Adopt this structure only when the additional abstraction improves testability. Do not move files merely to create a larger tree.

## Dependency management

Keep runtime and development dependencies explicit. Update the dependency declaration whenever imports change. Avoid unbounded version assumptions for critical browser tooling. A lockfile may be appropriate if this project grows into a reproducible application.

## Pull request expectations

Every behavior change should state what changed, how it was tested, which browser and driver were used, and which limitations remain. Tests should run locally or on mock pages. Live checks require explicit authorization and must not submit checkout or payment actions.
