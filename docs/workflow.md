# Automation Workflow

## Purpose

This guide documents the exact sequence currently implemented by `main.py`. It is not a guarantee that the live website will behave the same way when the script is executed.

## Step 1: Construct the automation object

The `AmazonCartAutomation` constructor stores a local driver path, sets a driver-related environment variable, creates a default Chrome service, starts Chrome, and deletes cookies.

**Important:** the stored path is not passed to the `ChromeService` constructor. Driver startup therefore depends on Selenium Manager or external driver discovery rather than that attribute.

## Step 2: Prepare the browser

`setup()` calls `maximize_window()`. It does not validate browser capabilities, configure a profile, or set a page-load timeout.

## Step 3: Open the target

The workflow navigates directly to the US Amazon homepage. There is no configurable target host or region.

## Step 4: Search

The script locates the search box by the ID `twotabsearchtextbox`, sends the product string, and submits the form. It does not validate the query or confirm that the expected results page loaded.

## Step 5: Open a result

The script waits up to ten seconds for an element at a long absolute XPath and clicks it. The XPath assumes a particular DOM structure and a particular position of the result. Search ranking, sponsored placements, localization, and markup changes can invalidate this assumption.

## Step 6: Interact with a product-page control

The script waits up to 100 seconds for an element with ID `wishListMainButton` and clicks it. The code does not confirm the resulting state and does not prove that the action adds the product to a cart.

## Step 7: Close the browser

The entry point calls `close_browser()`, which calls `driver.quit()`. This happens only on the normal path. An exception before that call can leave a browser process running.

## Expected future workflow design

A safer and more testable design should:

- Default to a local mock page.
- Validate the target host before browser navigation.
- Centralize selectors in a page-object class.
- Wait for a meaningful page state rather than element presence alone.
- Verify the outcome using a non-sensitive, explicit assertion.
- Capture sanitized diagnostic evidence on failure.
- Always close the browser in a `finally` block.
- Avoid login, checkout, purchase, or safeguard-bypass operations.

Any new workflow should update this document and the tests in the same change.
