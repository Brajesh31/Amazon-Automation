# Roadmap

This roadmap lists candidate improvements. Items are not implemented until they exist in source code and have been validated.

## Priority 1: Correctness and portability

- [ ] Remove machine-specific driver paths.
- [ ] Use Selenium Manager or an explicitly supplied compatible ChromeDriver.
- [ ] Guarantee cleanup with `try/finally` or a context manager.
- [ ] Replace the absolute XPath with selectors validated against local HTML fixtures.
- [ ] Rename or correct the final interaction and verify its behavior in a controlled test.
- [ ] Introduce validated configuration for safe test scenarios.

## Priority 2: Testability

- [ ] Add unit tests using mocked WebDriver interfaces.
- [ ] Add local HTML fixtures for search and product pages.
- [ ] Test timeout and cleanup paths.
- [ ] Add linting and formatting checks with a documented toolchain.
- [ ] Record tested Python, Selenium, Chrome and driver versions.

## Priority 3: Maintainability

- [ ] Separate browser lifecycle from page interactions.
- [ ] Add structured, privacy-conscious logging.
- [ ] Define bounded timeouts and consistent error messages.
- [ ] Add a sanitized failure-evidence policy.
- [ ] Remove the committed driver binary after confirming no supported workflow depends on it.

## Non-goals

- Bypassing CAPTCHA, authentication, bot detection, rate limits, fraud controls or purchase safeguards.
- Unattended shopping, checkout, payment or bulk-purchase automation.
- Collecting account credentials, cookies or payment information.
