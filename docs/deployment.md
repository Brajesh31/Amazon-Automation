# Deployment

This project is not a server application. If it is run in CI or a scheduled environment, use an isolated worker with an approved browser image, pinned dependencies, a disposable profile, restricted network access, and explicit execution limits.

Do not deploy it as an unattended shopping bot. Store secrets in the platform's secret manager if future authorized tests need them, and redact screenshots and logs before retention.
