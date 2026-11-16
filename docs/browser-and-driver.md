# Browser and Driver Management

## Components

Selenium controls Chrome through the WebDriver protocol. The local runtime requires a Chrome installation and a compatible driver, discovered explicitly or through Selenium Manager.

## Current repository behavior

The constructor stores a developer-specific Linux path in `self.chromedriver_path` and sets `webdriver.chrome.driver`. It then constructs `ChromeService()` without passing the stored executable path. The path is therefore not wired into the service.

The repository also tracks a large platform-specific executable at `Drivers/chromedriver`. It may not run on other operating systems or match the installed Chrome version.

## Preferred approach

Use a current Selenium release and Selenium Manager where available. It can discover or obtain a compatible browser driver. Network restrictions or enterprise policy may affect this behavior.

When manual driver management is required, install a compatible binary from a trusted source and pass its validated path to the Service constructor. Do not hard-code a developer's home directory or assume a Linux executable is portable.

## Diagnostics

When investigating startup problems, record:

- Operating system and architecture.
- Python version.
- Selenium version.
- Chrome version.
- ChromeDriver version, if manually managed.
- Whether the driver is executable.
- Sanitized WebDriver exception details.

## Binary policy

Before removing the existing binary, verify no supported workflow relies on it. If obsolete, remove it in a separate reviewed change and document the driver-management approach. Do not replace it with an unpinned executable.

## Security

Obtain Chrome and driver components through trusted distribution channels. Keep them updated. Never commit browser profiles, cookies or local storage. Use disposable profiles for authorized test runs.
