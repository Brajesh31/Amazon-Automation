# API

There is no HTTP API. The Python class exposes three local methods:

- `setup()` maximizes the browser window.
- `search_and_add_to_cart(product_name)` performs the site interaction.
- `close_browser()` terminates the WebDriver session.

These methods currently depend on Amazon page structure and should be treated as an unstable external integration.
