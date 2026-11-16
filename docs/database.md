# Database and Persistence

## Current state

There is no database in this project. The repository contains no database driver, schema, migration, ORM model, connection configuration or persistence service.

The WebDriver session exists in process memory. The constructor deletes cookies in its browser session. The application does not store products, carts, users, searches or order records.

## Why no database is required

The current proof of concept runs one browser interaction sequence and does not require state between executions. A database would add operational complexity without solving the main reliability gaps.

## Possible future data

An authorized test harness might store minimal, non-sensitive execution metadata, such as run identifier, timestamps, browser version, scenario name and pass/fail outcome. Prefer short retention and avoid storing page contents.

Never persist authentication cookies, browser profiles, payment details, personal account data or sensitive page content. If persistence becomes necessary, establish purpose, access controls, encryption, retention, deletion and incident procedures before implementation.

## Migration policy

There is no migration system today. If a persistence layer is introduced, document schema ownership, migration tooling, backup and restore, data classification and deletion behavior.
