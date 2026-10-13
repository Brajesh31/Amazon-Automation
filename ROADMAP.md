# Roadmap

## Near term

- Add `requirements.txt` or a lockfile with a documented supported Python range.
- Make the driver path configurable and use `ChromeService(executable_path=...)`.
- Replace absolute XPaths with resilient, tested selectors.
- Add `try/finally` cleanup and structured logging.

## Future

- Add a local mock storefront and offline tests for browser flows.
- Parameterize region, search term, and selectors without embedding account data.
- Add accessibility-aware test scenarios and failure screenshots for authorized test environments.
