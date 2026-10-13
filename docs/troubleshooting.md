# Troubleshooting

## ChromeDriver cannot start

Check Chrome and ChromeDriver compatibility, confirm the executable path, and ensure the driver can be launched by the current user. Selenium Manager may locate a compatible driver when the code does not override service configuration.

## The search element cannot be found

The site may show a consent page, regional landing page, login prompt, or changed markup. Inspect the page in an authorized test environment and update selectors only after confirming the intended flow.

## The first product cannot be opened

The absolute XPath is brittle and can change with experiments, personalization, or regional results. Replace it with a stable selector and a page-object test against a controlled fixture.

## The cart action fails

The current element ID may refer to a wishlist or another control rather than the cart. Do not broaden the automation to bypass interstitials or safeguards; use a mock page for development.
