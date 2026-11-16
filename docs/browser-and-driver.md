# Browser and Driver Management

## Components

Selenium automates a browser through the WebDriver protocol. For Chrome, this involves:

1. A Chrome browser installation.
2. A compatible ChromeDriver executable, located explicitly or discovered by Selenium Manager.
3. The Selenium Python package.
4. A local WebDriver session managed by the Python process.

A mismatch between Chrome and ChromeDriver versions can prevent the browser from starting.

## What this repository currently does

The constructor contains a developer-specific Linux path in `self.chromedriver_path` and sets `webdriver.chrome.driver`. However, it then constructs `ChromeService()` without passing that path. The code does not explicitly connect the stored path to the service.

The repository also tracks `Drivers/chromedriver`, a large platform-specific executable. It may be incompatible with other systems or browser versions. It should not be considered a portable dependency.

## Recommended local approach

Use a current Selenium release and its Selenium Manager support where possible. Selenium Manager can discover or obtain a compatible driver as part of WebDriver initialization. Network and policy restrictions may affect this behavior.

Where an explicitly installed driver is required, configure the service with a validated executable path. Do not hard-code a developer's home directory or assume that a Linux binary will run on Windows or macOS.

## Diagnostics

Record these values when investigating startup failures:

- Operating system and architecture.
- Python version.
- Selenium version.
- Chrome version.
- ChromeDriver version, if manually managed.
- Whether the process can execute the driver.
- Exact WebDriver exception, with user-specific paths and secrets redacted.

## Binary handling

Before removing the committed binary, verify whether any supported workflow explicitly depends on it. If it is no longer required, remove it in a separate reviewed change and add a clear dependency policy. Avoid replacing it with another unpinned executable.

## Security

Download browser and driver components only from trusted distribution channels. Keep them patched. Do not commit browser profiles, cookies, local storage, or session state. Use disposable profiles for authorized tests.
