# Operations Runbook

## Pre-flight checklist

- Confirm that the target environment is authorized for browser automation.
- Review the target host and test search input.
- Verify Python and Selenium are installed in the intended virtual environment.
- Confirm Chrome starts.
- Confirm driver compatibility or Selenium Manager availability.
- Use a disposable browser profile.
- Ensure the run cannot sign in, check out, pay or bypass a safety control.

## Execute

Run from the repository root:

```bash
python main.py
```

The current script uses a hard-coded search phrase and does not accept command-line configuration.

## Observe

Watch for browser startup errors, timeouts, element lookup failures and unexpected pages. Stop if the target blocks or challenges automation. Do not attempt to defeat those controls.

## Stop and cleanup

On the normal path, the script calls `driver.quit()`. If an exception occurs before that point, close the browser process manually. A future implementation should guarantee cleanup in `finally`.

Remove temporary profiles and screenshots after checking whether they contain sensitive information. Never retain session state without a documented authorized purpose.

## Incident procedure

If the workflow performs an unexpected interaction:

1. Stop execution and close the browser.
2. Do not repeat the action on a real account to reproduce it.
3. Preserve only sanitized diagnostic information.
4. Remove accidentally captured secrets from local artifacts and rotate any exposed credential.
5. Report the relevant code path and sanitized conditions to the maintainer.

## Operational risk

The current final selector does not prove a cart operation. Do not use the script for purchasing or unattended shopping. It remains a prototype until tested behavior is implemented and verified safely.
