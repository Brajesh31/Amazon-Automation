# Amazon Cart Automation

Amazon Cart Automation is a small Python/Selenium proof of concept that opens Amazon, searches for a product, opens the first result, and attempts to add it to a cart. It is intended for browser-automation learning and test-environment experimentation.

> Use this project only where you have permission and in accordance with Amazon's terms, applicable laws, and the site's robots and anti-automation controls. Do not use it to bypass authentication, rate limits, CAPTCHAs, or purchase safeguards.

## How it works

[`main.py`](./main.py) defines `AmazonCartAutomation`:

1. Creates a Chrome WebDriver.
2. Clears browser cookies.
3. Opens `https://www.amazon.com/`.
4. Searches for `Wireless Earbuds`.
5. Opens a hard-coded first-result XPath.
6. Clicks a wishlist/cart-related element and closes the browser.

The code is a demonstration rather than a reliable production test. Amazon's markup, regional behavior, consent screens, login requirements, and anti-bot controls can change at any time.

## Setup

Use Python 3.10 or a compatible modern Python release and install Selenium:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
python -m pip install selenium
```

Install Google Chrome and ensure its version is compatible with ChromeDriver. The current script contains a machine-specific Linux driver path; update it for your environment before running.

## Run

```bash
python main.py
```

The script launches a visible browser and uses a real public site. Run it only with test-safe search terms and never with an account or payment flow unless you have explicit authorization.

## Known limitations

- The ChromeDriver path is hard-coded and the bundled `Drivers/chromedriver` is platform-specific.
- `ChromeService()` does not currently pass the configured path, so driver discovery may depend on Selenium Manager or `PATH`.
- Selectors are brittle and tied to current Amazon markup.
- The element ID `wishListMainButton` may not represent adding an item to the cart.
- There is no configuration file, dependency lockfile, test suite, retry policy, screenshot capture, or guaranteed cleanup on exceptions.

See [`docs/development.md`](./docs/development.md), [`docs/troubleshooting.md`](./docs/troubleshooting.md), and [`SECURITY.md`](./SECURITY.md) before extending the script.

## License

The project is released under the MIT License. See [`LICENSE`](./LICENSE).

Last updated: 2026-10-24 22:53 UTC
