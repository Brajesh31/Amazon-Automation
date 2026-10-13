# Development

Use a page-object or helper abstraction before adding additional flows. Keep selectors centralized, use `WebDriverWait` with meaningful expected conditions, and make the target URL and safe test data configurable.

For local checks:

```bash
python -m py_compile main.py
```

Prefer mock HTML fixtures for repeatable tests. If live-site validation is necessary, obtain permission first, use a disposable profile, avoid login and purchase actions, and record the exact browser and driver versions.
