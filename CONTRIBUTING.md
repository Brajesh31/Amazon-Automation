# Contributing

Thank you for helping improve Amazon Cart Automation. Keep contributions focused on safe browser-automation education, correctness, maintainability and accurate documentation.

## Before making a change

1. Read the [README](README.md), [Security Policy](SECURITY.md), and relevant technical guides.
2. Confirm that the intended target and test environment are authorized.
3. Check for an existing issue or explain the purpose of the change.
4. Keep each change focused and describe behavior differences.

## Development standards

- Use clear Python names and readable functions.
- Separate configuration from browser interaction.
- Centralize selectors rather than scattering raw XPath expressions.
- Prefer Selenium explicit waits over arbitrary sleeps.
- Guarantee that the browser closes on both success and failure.
- Keep runtime packages declared in `requirements.txt`.
- Do not commit local paths, browser binaries unless strictly required, secrets, browser profiles, cookies, downloads or screenshots containing personal data.
- Keep documentation consistent with implemented behavior.
- Do not claim that an item is added to a cart unless a controlled test proves the behavior.

## Safety restrictions

Do not add functionality to bypass authentication, MFA, CAPTCHA, anti-bot controls, rate limits, fraud safeguards, purchase confirmation or regional restrictions. Do not add checkout, payment submission, bulk purchasing or account-abuse workflows.

## Local validation

```bash
python -m py_compile main.py
python -m pip check
```

Add mock-based tests for new behavior where feasible. Do not use a live shopping website as an uncontrolled test fixture.

## Pull request checklist

- [ ] The change has a clear, authorized purpose.
- [ ] Code and documentation describe actual behavior.
- [ ] Static checks pass.
- [ ] Tests use mocks or an approved test environment.
- [ ] Browser cleanup is handled on failure.
- [ ] No secrets, personal data or browser state are included.
- [ ] Known limitations are documented.
