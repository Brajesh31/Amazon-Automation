# FAQ

## Does this place an order?

The current script does not implement checkout or payment submission, but it does interact with a live shopping page. Use it only with permission and safe, non-purchasing test data.

## Why is the driver path not portable?

The original script contains a machine-specific Linux path. Driver discovery and configuration should be made explicit and platform-aware before reuse.

## Can this run unattended?

It should not be used as an unattended shopping bot. Authorized test automation should run with rate limits, an isolated profile, explicit scope, and a controlled target.

## Where should secrets go?

Nowhere in source files. Use a secret manager or environment variables for future authorized integrations, and keep `.env` files ignored.
