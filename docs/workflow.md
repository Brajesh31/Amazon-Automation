# 🔄 Automation Workflow

## Purpose and scope

This guide records the exact sequence currently implemented in `main.py`. It is not a promise that the live website behaves consistently or that the final operation succeeds.

## 1. Construct the automation object

The constructor stores a developer-specific driver path, sets a driver-related environment variable, builds a default Chrome service, starts Chrome, and deletes cookies in that browser session.

The configured path is not passed to `ChromeService`. Browser startup therefore depends on default driver discovery or Selenium Manager.

## 2. Prepare the browser

`setup()` maximizes the window. It does not explicitly configure a profile, page-load timeout, download directory, or browser capabilities.

## 3. Open the target site

The method navigates to the fixed US Amazon homepage. The target region and URL are not configurable.

## 4. Search

The workflow locates the search input by ID `twotabsearchtextbox`, enters the supplied product string and submits the form. It does not validate the query or assert that the expected search results loaded.

## 5. Open a result

The code waits up to ten seconds for an element identified by an absolute XPath and clicks it. Absolute XPaths are coupled to a specific page layout and search-result order. Sponsored placements, localization, experiments and DOM changes may invalidate it.

## 6. Interact with product page

The workflow waits up to 100 seconds for an element with ID `wishListMainButton` and clicks it. The code does not verify the resulting state. The selector does not establish that an item was added to the shopping cart.

## 7. Close browser

The entry point calls `close_browser()`, which invokes `driver.quit()`. This occurs only on the normal path. If an earlier operation raises an exception, browser cleanup may not run.

## Safer future workflow

- Default behavior should use a local mock storefront.
- Validate the target host before navigation.
- Centralize selectors in a page-object abstraction.
- Wait for observable page state, not merely element presence.
- Verify outcomes in a controlled test fixture.
- Guarantee cleanup with `finally` or a context manager.
- Capture sanitized diagnostics only.
- Do not automate login, checkout, payment, purchasing or bypasses of safeguards.

Update this guide and the tests whenever the workflow changes.
