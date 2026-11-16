# ❓ Frequently Asked Questions

## Is this production-ready?

No. It is a small Selenium proof of concept with hard-coded configuration, brittle selectors, incomplete cleanup guarantees and no automated behavior tests.

## Does it definitely add an item to the cart?

No. The code clicks an element with ID `wishListMainButton`. It does not verify cart state, so the method name should not be treated as proof of an add-to-cart operation.

## Why does the driver path appear ineffective?

The path is assigned to an attribute, but `ChromeService()` is constructed without that executable path. Startup therefore uses default discovery or Selenium Manager.

## Why is a driver binary committed?

The repository currently tracks a platform-specific binary. It is not portable and may not match your installed Chrome. Prefer Selenium Manager or an explicitly managed compatible driver. Consider removing the binary in a separate reviewed change after checking for workflow dependencies.

## Is a database required?

No. The script does not maintain durable application data, products, carts or orders.

## Does the project expose an API?

No HTTP API exists. The only interface is the local Python class in `main.py`.

## Can it run in GitHub Actions?

CI currently checks source syntax, dependencies and documentation only. It does not run the live browser workflow. Browser tests should use a local mock.

## Should I use my personal shopping account?

No. This prototype should not be used with personal shopping or payment accounts. Prefer mock pages or an explicitly authorized sandbox.

## What if the website blocks automation?

Stop the run. Do not bypass CAPTCHA, anti-bot systems, rate limits, authentication or other safeguards.

## Where should I report a bug?

Read [SUPPORT.md](../SUPPORT.md). Provide sanitized environment details. Never attach cookies, browser profiles, credentials, account identifiers or payment information.
