# Testing Strategy

## Current test coverage

There is no automated unit, integration, or end-to-end test suite in the repository. A Python syntax check is available, but it does not verify browser startup, selector correctness, or the result of an interaction.

## Static checks

Run:

```bash
python -m py_compile main.py
python -m pip check
```

The GitHub Actions workflow runs the syntax check and verifies the presence of required documentation. It does not access the live website.

## Recommended testing layers

### 1. Unit tests

Test pure logic after configuration and workflow logic are extracted from the WebDriver class. Use mocks for browser and page dependencies. Unit tests should not create a real Chrome process or make network requests.

### 2. Mock-page tests

Create local HTML fixtures representing the expected search form and product result. Serve them locally or load them through a controlled test setup. Verify that selectors and wait conditions behave as expected.

### 3. Browser lifecycle tests

Use a mocked driver factory to verify that the driver is quit when navigation or lookup fails. This is especially important because the current script only closes the browser on the success path.

### 4. Authorized integration tests

Only run against a site or sandbox where browser automation is explicitly permitted. Use a disposable profile and safe test data. Do not log in to a personal shopping account or attempt checkout, payment, or safeguard bypasses.

## Test design requirements

- Avoid dependence on live product ranking.
- Avoid absolute XPath selectors.
- Assert observable and documented outcomes.
- Keep test data non-sensitive.
- Do not include session cookies or browser profile directories in test artifacts.
- Make all waits bounded.
- Ensure the browser quits after both success and failure.

## Current CI boundary

CI validates repository integrity and Python syntax using a controlled runner. It intentionally does not run the live Amazon workflow. A CI green check is not evidence that the live site selectors work.
