# CLAUDE.md

Playwright + pytest regression suite for https://www.saucedemo.com (UI) and a
`requests`-based suite for https://restful-booker.herokuapp.com (API). Both
targets are live third-party sites, not mocks - they can change under us.

## Commands

Windows venv; run from the repo root:

```bash
./venv/Scripts/python.exe -m pytest              # everything, headless
./venv/Scripts/python.exe -m pytest -m api       # API only, no browser needed
./venv/Scripts/python.exe -m pytest -m "login or smoke" --tb=short
./venv/Scripts/python.exe -m pytest --headed --slowmo=1000   # watch a run
```

Markers are registered in `pytest.ini` (login, inventory, cart, checkout,
smoke, mobile, api, auth, booking). Every run overwrites `report.html`
(gitignored).

## Layout

- `pages/` - page objects (UI). All locators live here, not in tests.
- `api/` - client objects (API), same idea as the page objects.
- `tests/conftest.py` - fixtures. Use `logged_in_user`: it logs in *and waits
  for the inventory to render*, so tests never start on a half-loaded page.
- `test-plans/*.csv` - manual test plans; each row links to its automated test
  in `Automated Test Reference`.

## Rules for changing tests

- **Never weaken an assertion to make a test pass.** Fix the locator, the
  wait, or report the app bug. Removing or loosening a check needs the user's
  say-so.
- **Wait, don't snapshot.** `locator.count()`, `is_visible()` and `page.url`
  read the page *right now* and don't retry. Use `expect(...)` (auto-retrying).
  `inner_text()` and `click()` do wait, so they're fine.
- **A negative check needs a positive wait first.** `not_to_be_visible()` or
  `to_have_count(0)` pass instantly on a page that hasn't rendered - or after
  a failed login. Wait for something that proves the page is ready, then assert
  the absence.
- **Prefer stable locators** (`id`, `data-test`) over roles/text. The site
  once changed its product links to `role="button"` and broke
  `get_by_role("link")`.
- **New behaviour = new test + test-plan row + README mention** (new page
  objects go in the README structure listing).
- **Mutation-check new tests.** Temporarily sabotage the behaviour the test
  guards (wrong password, skip the click, submit valid data) and confirm the
  test fails, then restore. A test that stays green when the feature is broken
  is worthless.

## Debugging a failure

1. `git status` / `git diff` first: is it your change or already broken at HEAD?
2. Look at the live DOM (a short Playwright script) before "fixing" a locator -
   the site may have changed, or your locator may just be wrong.
3. Form a hypothesis, then test it (e.g. run 10 times to rule flaky in or out).
4. When an exploratory probe surprises you, re-run it with proper waits before
   reporting it - several first-pass "findings" were just unwaited snapshots.
5. Re-run the **full** suite, not just the touched tests.

## CI and publishing

GitHub Actions runs the full suite on push/PR to `main` and `develop`. Pushes
to `main` also publish `report.html` to the public GitHub Pages site, so
commit freely but **push only when the user asks**. `gh` isn't installed; check
a run through the API:

```bash
curl -s "https://api.github.com/repos/fegero585/saucedemo-regression-tests/actions/runs?head_sha=$(git rev-parse HEAD)"
```

## Deliberately not covered / open questions

- `problem_user`, `error_user`, `visual_user`, `performance_glitch_user`:
  intentional demo defects, skipped on purpose.
- Cart contents persisting across logout/login, and checkout accepting `abc`
  as a postal code or whitespace-only names: observed, but whether they're
  bugs is a product decision. Don't add tests asserting either way without
  asking.

## Windows notes

Git prints "LF will be replaced by CRLF" warnings; they're harmless. The CSV
test plans use CRLF row terminators - append with Python's `csv` module
(`lineterminator="\r\n"`) rather than by hand.
