# Local Python Interface

## No HTTP API

This repository does not expose an HTTP server, REST endpoint, GraphQL API, webhook, or network service. The term "API" in this document refers only to the Python class methods in `main.py`.

## Class: `AmazonCartAutomation`

### Constructor

```python
AmazonCartAutomation()
```

Creates a Chrome WebDriver session and deletes cookies from that browser session. It currently stores a machine-specific driver path but does not pass it to the `ChromeService` object.

The constructor has no parameters for target URL, browser options, timeout, driver path, or profile directory.

### `setup()`

```python
automation.setup()
```

Maximizes the browser window. It returns no value and performs no explicit readiness validation.

### `search_and_add_to_cart(product_name)`

```python
automation.search_and_add_to_cart("Wireless Earbuds")
```

Navigates to the hard-coded Amazon US homepage, searches the supplied string, opens a result selected by an absolute XPath, and clicks an element identified as `wishListMainButton`.

The name is not proof of the final behavior. The method currently does not verify that an item is present in the shopping cart.

### `close_browser()`

```python
automation.close_browser()
```

Calls `quit()` on the Selenium WebDriver. It should be called even if an earlier step fails. The current top-level script does not use a `finally` block.

## Exceptions

The methods do not define a project-specific exception hierarchy. Selenium, browser startup, network, timeout, and element lookup exceptions may propagate to the caller.

## Compatibility

These methods are an internal prototype interface. They are not documented as a stable package API and may change as the project is refactored.
