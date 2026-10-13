# Architecture

The project is a single Python module with one class, `AmazonCartAutomation`. The constructor creates a Selenium Chrome driver; `setup()` prepares the window; `search_and_add_to_cart()` performs the browser flow; and `close_browser()` quits the driver.

The current architecture has no service layer, configuration object, page-object model, test fixture, persistence, or API. The browser is the only runtime dependency beyond Python, Selenium, Chrome, and a compatible driver.
