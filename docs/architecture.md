# 🏗️ Architecture

## Overview

Amazon Cart Automation is a single-module Python program built around Selenium WebDriver. It currently has no internal service network, API server, database, task queue, frontend, or persistence layer.

The entry point is `main.py`. It defines `AmazonCartAutomation` and creates an instance from the module's `__main__` block.

## Runtime components

| Component | Responsibility | Current implementation |
|---|---|---|
| Python | Executes the script | Local interpreter |
| Selenium | Controls the browser | Selenium Python package |
| Chrome | Renders the remote page | Installed system browser |
| ChromeDriver / Selenium Manager | WebDriver bridge and driver discovery | Bundled binary exists; service uses default discovery |
| Automation class | Owns browser and interaction methods | `AmazonCartAutomation` |
| Target page | External DOM and user-facing controls | Live external dependency |

## Execution sequence

1. The module constructs an `AmazonCartAutomation` instance.
2. The constructor stores a machine-specific driver path, sets an environment variable, creates a default Chrome service, starts Chrome, and deletes session cookies.
3. `setup()` maximizes the browser window.
4. `search_and_add_to_cart()` opens the homepage, locates the search box, submits a query, clicks a first-result link, then clicks a product-page element.
5. `close_browser()` calls `quit()`.

The method name overstates the final behavior. The selector is `wishListMainButton`; there is no assertion that a cart update took place.

## External boundary

The target site is independent of this repository. Markup, consent screens, regional settings, login prompts, experiments and anti-automation controls can change. There is no stable API contract with the external page.

Treat DOM changes as integration changes. Validate selectors against controlled fixtures first and only run live checks when explicitly authorized.

## State and persistence

The WebDriver exists in memory while the Python process runs. The constructor deletes cookies in the active browser session. No product, cart, account, cookie or order state is persisted by the application. There is no database.

## Lifecycle and errors

The current entry point calls `close_browser()` only after the interaction returns normally. Exceptions may prevent cleanup. A future implementation should use `try/finally` or a context manager.

## Current architectural gaps

- One file combines setup, navigation, selectors and orchestration.
- Configuration is embedded in source.
- Selectors are not centralized.
- Driver setup is not portable.
- No page-object abstraction or domain model exists.
- No automated tests or mock pages exist.
- No structured logging or standard error model exists.

## Recommended evolution

Extract configuration, browser lifecycle and page interaction only when it improves testability. Keep external browser operations behind a small adapter. Add local HTML fixtures and tests that do not make live shopping changes. Do not add checkout or payment automation.
