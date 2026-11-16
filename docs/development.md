# Development Guide

## Development goals

Keep this repository a small Selenium learning project. Prioritize portability, clear behavior, safe configuration, browser lifecycle correctness and repeatable tests. Avoid broad or unattended automation against live shopping workflows.

## Conventions

- Use readable Python and descriptive names.
- Separate configuration from page interaction.
- Centralize selectors.
- Prefer explicit waits and meaningful expected conditions over arbitrary sleeps.
- Ensure drivers close on success and failure.
- Declare runtime dependencies in `requirements.txt`.
- Do not commit local paths, secrets, browser profiles, cookies, downloads or personal screenshots.
- Document behavior as it exists, not as intended.

## Local development loop

1. Create and activate a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Make a focused change.
4. Run `python -m py_compile main.py`.
5. Run `python -m pip check`.
6. Add a mock-based test for changed behavior.
7. Review the diff for generated files, user data and false claims.
8. Update relevant docs and `CHANGELOG.md`.

## Current source boundaries

`main.py` currently owns browser creation, navigation, selectors and top-level orchestration. The method called `search_and_add_to_cart` does not verify that a cart update occurs. Do not write a passing test for cart behavior until the implementation and its controlled fixture prove that behavior.

## Possible future package structure

This is a proposal, not a description of files currently present:

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

Create this structure only when each layer provides testability or separation of concerns. Avoid adding empty folders or abstractions for appearance.

## Dependency management

Keep imported packages declared. Document Python support and tested browser combinations. Update the dependency declaration when code imports change. Consider a lockfile if reproducible releases become a requirement.

## Contribution expectations

Describe the behavior change, validation method, browser and driver versions, and remaining limitations. Tests should use a local mock or explicitly authorized test environment. Do not include live shopping or payment actions.
