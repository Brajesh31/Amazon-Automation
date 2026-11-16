# 🩺 Troubleshooting

## Chrome cannot start

Check that Chrome is installed and executable. Verify Selenium and browser versions. If manually managing the driver, check compatibility and executable permissions.

The current script stores a driver path but does not pass it to `ChromeService`. Use Selenium Manager or explicitly configure a validated executable path.

## Driver version mismatch

Chrome and ChromeDriver must be compatible. The committed binary may not match your browser or operating system. Prefer Selenium Manager or a manually managed driver from a trusted distribution channel.

## Search field not found

The site may have displayed a consent page, regional landing page or changed markup. Inspect the page only in an authorized test environment. Do not bypass an access challenge.

## Timeout while opening the first result

The absolute XPath is fragile. Result order and page structure can change. Update and test selectors against a local fixture. Do not increase timeouts indefinitely.

## Product page control not found

The page may differ from the assumed layout. The current selector is not a verified cart selector. Do not substitute arbitrary controls or bypass site safeguards.

## Browser remains open after an exception

The current script only calls `close_browser()` on the normal path. Close the browser manually. A code improvement should use `try/finally` or a context manager.

## Syntax error

```bash
python -m py_compile main.py
```

Check that the intended Python interpreter is active.

## Dependency errors

```bash
python -m pip install -r requirements.txt
python -m pip check
```

Use `python -m pip` to ensure packages install into the same interpreter used to execute the script.

## Bug report details

Include OS and architecture, Python/Selenium/Chrome/driver versions, command used and a sanitized traceback. Never provide cookies, profiles, account credentials or payment information.
