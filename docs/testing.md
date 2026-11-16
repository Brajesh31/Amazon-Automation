# Testing Strategy

## Existing coverage

There is currently no automated unit, integration or end-to-end test suite. A Python syntax check is available, but it does not prove browser startup, selector correctness or successful interaction with a product page.

## Static checks

```bash
python -m py_compile main.py
python -m pip check
```

GitHub Actions performs static validation and documentation integrity checks. It does not connect to Amazon or perform shopping actions.

## Recommended test layers

### Unit tests

After separating configuration and workflow logic from WebDriver operations, test pure logic and error handling with mocks. Unit tests should not start a real browser or make network requests.

### Mock page tests

Use local HTML fixtures for the search form and product result. Load them in a controlled browser test or use a local test server. This makes selector behavior repeatable without depending on public search results.

### Lifecycle tests

Use a mocked driver factory to assert that `quit()` is called after both successful runs and exceptions. This is important because the current entry point can leave Chrome open when an earlier action fails.

### Authorized browser integration tests

Run only against a sandbox or target where automation is explicitly permitted. Use disposable profiles and non-sensitive data. Do not sign in to personal shopping accounts or attempt checkout, payment or safeguard bypasses.

## Test quality requirements

- Avoid live product ranking and changing public DOM as test data.
- Avoid absolute XPath selectors.
- Assert documented outcomes.
- Keep waits bounded.
- Do not capture session cookies, browser profiles or account content.
- Guarantee browser cleanup after all test paths.

## CI boundary

A successful CI run means the configured repository checks passed. It does not prove the live website selectors still work or that the final element click changes cart state.
