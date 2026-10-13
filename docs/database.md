# Database

The project has no database and does not persist products, carts, accounts, or orders. Selenium cookies are cleared when the driver starts, and no application data store is configured.

Do not introduce persistence for session cookies or customer data without a documented threat model, explicit authorization, encryption, retention limits, and a security review.
