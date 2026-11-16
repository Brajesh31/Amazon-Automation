# Architecture

## 1. Overview

Amazon Cart Automation is currently a single-module Python program built around Selenium WebDriver. Its architecture is intentionally small and has no internal service network, API server, database, task queue, frontend, or persistence layer.

The main entry point is `main.py`. It defines one class, `AmazonCartAutomation`, and invokes that class from the module's `__main__` block.

## 2. Runtime components

| Component | Responsibility | Current implementation |
|---|---|---|
| Python runtime | Executes the script | Local Python interpreter |
| Selenium | Controls browser through WebDriver | Imported from `selenium` |
| Chrome | Renders the remote website | Installed system browser |
| ChromeDriver / Selenium Manager | WebDriver protocol bridge and driver discovery | A driver binary exists in the repository; service configuration currently relies on default discovery |
| Automation class | Owns browser and interaction methods | `AmazonCartAutomation` |
| Amazon page | External DOM and user-facing controls | Live external dependency |

## 3. Execution flow

1. The module creates an `AmazonCartAutomation` instance.
2. Its constructor stores a machine-specific driver path, sets an environment variable, constructs a default Chrome service, creates Chrome, and deletes session cookies.
3. `setup()` maximizes the browser window.
4. `search_and_add_to_cart()` opens the homepage, locates a search field, enters a query, submits the form, clicks a first-result link, and interacts with a product-page element.
5. `close_browser()` calls `quit()` on the WebDriver.

The method name overstates the current behavior. The final selector is `wishListMainButton`, so the code does not prove that it adds an item to a shopping cart.

## 4. External boundary

The external website is not controlled by this repository. Markup, selectors, consent screens, regional settings, login requirements, experiments, and anti-automation controls may change independently. The script has no adapter contract or stable API with the site.

A change to the target DOM should be treated as an integration change, not as an ordinary internal refactor. Validate against a controlled fixture first and only run live checks when explicitly authorized.

## 5. State and persistence

The script holds a WebDriver object in memory. It does not persist product data, cart state, user accounts, cookies, or order records. The constructor deletes cookies from the active browser session. There is no database or file-backed state store.

## 6. Error and lifecycle model

The current entry point calls `close_browser()` only after the search method returns normally. If browser creation or an interaction raises an exception, the cleanup method may not execute. Future changes should manage the WebDriver with a context manager or `try/finally`.

## 7. Architectural limitations

- One file combines browser setup, navigation, selectors, and orchestration.
- Configuration is embedded in source code.
- Selectors are embedded in interaction code.
- Driver setup is not portable.
- No typed domain model describes a product, cart, or test result.
- There are no automated tests or mock pages.
- No structured logging or standardized error model exists.

## 8. Recommended evolution

A safe, maintainable next step is to extract configuration, browser lifecycle management, a page-object abstraction, and a local mock page. Keep external interactions behind a small adapter. Add tests for selectors and lifecycle behavior without making live shopping changes. Do not add checkout or payment automation.
