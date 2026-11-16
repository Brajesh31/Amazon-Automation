# Local Python Interface

## No HTTP API

This project does not expose an HTTP server, REST API, GraphQL API, webhook, or network service. This document describes only the local Python class in `main.py`.

## `AmazonCartAutomation()`

The constructor creates a Chrome WebDriver session and deletes cookies from that session. It stores a machine-specific driver path but does not pass the path to the `ChromeService` instance. There are no constructor parameters for browser options, URL, timeout, driver path or profile directory.

## `setup()`

```python
automation.setup()
```

Maximizes the browser window. It returns no value and does not validate page readiness.

## `search_and_add_to_cart(product_name)`

```python
automation.search_and_add_to_cart("Wireless Earbuds")
```

Navigates to the hard-coded Amazon US homepage, submits a search, clicks an absolute-XPath result, and clicks an element identified by `wishListMainButton`.

The method name is not evidence of a successful cart operation. The implementation does not verify cart state.

## `close_browser()`

```python
automation.close_browser()
```

Calls `quit()` on the WebDriver. The current entry point does not protect this call with a `finally` block.

## Exceptions and compatibility

The class does not define a project-specific exception hierarchy. Selenium and browser startup, timeout, navigation and element lookup errors may propagate directly. These methods are an internal prototype interface, not a stable public package API.
