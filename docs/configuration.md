# Configuration

## Current configuration

The current script is not environment-driven. The following values are embedded in `main.py`:

| Setting | Current value | Location | Notes |
|---|---|---|---|
| Homepage | `https://www.amazon.com/` | `search_and_add_to_cart` | US domain is hard-coded |
| Search term | `Wireless Earbuds` | `__main__` block | Not supplied by command-line arguments |
| Search field selector | `twotabsearchtextbox` | `search_and_add_to_cart` | Site-specific ID |
| First product selector | Absolute XPath | `search_and_add_to_cart` | Highly fragile |
| Product-page action | `wishListMainButton` | `search_and_add_to_cart` | Does not verify cart behavior |
| Driver path | Developer-specific absolute path | Constructor | Not portable |
| Wait values | 10 and 100 seconds | Interaction method | Hard-coded |

## Environment example

`.env.example` is informational only. The Python program does not currently load it. Adding values to that file will not change runtime behavior.

Never add credentials, session cookies, account tokens, card details, or personal information to the example file.

## Recommended future configuration

For authorized mock or test use, a future configuration object could expose:

- A test base URL, defaulting to a local mock rather than a public shopping site.
- A non-sensitive search term.
- Browser visibility/headless mode for controlled tests.
- Explicit wait timeout.
- Browser binary path where required.
- A disposable profile directory.
- Screenshot output directory with a retention policy.

Validate all configuration at startup. Reject unexpected schemes and unapproved target hosts. Avoid accepting arbitrary external URLs from untrusted input.

## Driver configuration

The constructor currently assigns a path to `self.chromedriver_path`, but creates `ChromeService()` without that executable path. The assignment is therefore not wired into the Service object. Prefer Selenium Manager for local development or pass an explicitly validated driver path to the Service constructor. Details are in [Browser and driver management](browser-and-driver.md).
