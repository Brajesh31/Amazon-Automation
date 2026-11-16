# Configuration

## Current behavior

The script does not load environment variables, a TOML/YAML file, command-line options or a configuration object. Important values are embedded in `main.py`.

| Setting | Value | Current location | Limitation |
|---|---|---|---|
| Target URL | `https://www.amazon.com/` | Workflow method | Fixed US domain |
| Product query | `Wireless Earbuds` | Entry point | Hard-coded |
| Search selector | `twotabsearchtextbox` | Workflow method | External DOM dependency |
| Result selector | Absolute XPath | Workflow method | Highly fragile |
| Product action selector | `wishListMainButton` | Workflow method | Not verified as cart action |
| Driver path | Developer-specific absolute path | Constructor | Not portable |
| Wait duration | 10 and 100 seconds | Workflow method | Hard-coded |

## Environment example

`.env.example` is informational only. The program does not load it. Adding keys to the file will not affect execution.

Never add passwords, cookies, account tokens, payment data or personal information to configuration examples.

## Recommended future settings

For an authorized mock/test workflow, a future configuration could include a local test base URL, non-sensitive search term, page timeout, browser visibility, explicit driver path where needed, and temporary profile directory.

Validate configuration at startup. Restrict allowed target hosts and URL schemes. Do not accept arbitrary destinations from untrusted input.

## Driver configuration

The code assigns a path to `self.chromedriver_path` but calls `ChromeService()` without passing it. Use Selenium Manager or pass a validated executable path to the service constructor. See [Browser and driver management](browser-and-driver.md).
