# ⚠️ Known Limitations

## Functional

- The target URL is the US Amazon homepage and is hard-coded.
- The product search phrase is hard-coded in the entry point.
- The first result is selected with an absolute XPath.
- The final control is `wishListMainButton`; the program does not verify cart state.
- There is no check that the expected search or product page has loaded.

## Portability

- A developer-specific Linux driver path appears in source.
- That path is not passed to `ChromeService`.
- A platform-specific ChromeDriver executable is tracked in the repository.
- No tested operating-system and browser compatibility matrix is defined.

## Reliability

- Browser cleanup is not protected by `finally`.
- There is no central timeout or retry policy.
- There is no structured error model.
- There is no screenshot redaction or artifact-retention policy.
- External page markup and access conditions can change.

## Quality

- No automated behavior tests or mock HTML fixtures exist.
- No formatter, linter or static type checker is configured.
- Dependencies are not fully locked.
- CI does not launch Chrome or perform live-site checks.

## Absent capabilities

- No database or persistence.
- No HTTP API.
- No scheduler, task queue, monitoring or frontend.
- No user management.
- No checkout, payment, purchase or order-management feature.

## Remediation priority

Prioritize driver portability, explicit configuration, exception-safe cleanup, stable selectors and mock-based tests. Do not attempt to improve reliability by bypassing access controls or generating more traffic against the live site.
