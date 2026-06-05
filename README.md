# saucedemo-playwright-py

> ℹ️ **Why does this repo exist?**
>
> The real test suites are locked behind NDAs - which is great for clients, less great for anyone
> trying to verify I actually know what I'm doing.
> Enter SauceDemo: a site built to be tested, with credentials in the docs and no production data at risk.
> Same approach, same patterns - just without the legal paperwork.

---

Automated end-to-end tests for [saucedemo.com](https://www.saucedemo.com) built with [Playwright](https://playwright.dev/python/) and [pytest](https://pytest.org), following the Page Object Model pattern.

## Test coverage

| Group | Cases | Status |
|-------|-------|--------|
| Login | TC01 - TC07 | ✅ Done |
| Inventory | TC08 - TC13 | ✅ Done |
| Product details | TC14 - TC17 | ✅ Done |
| Cart | TC18 - TC23 | ✅ Done |
| Checkout - form | TC24 - TC27 | ⬜ Pending |
| Checkout - summary & order | TC28 - TC31 | ⬜ Pending |
| Logout & navigation | TC32 - TC35 | ⬜ Pending |
| Special users | TC36 - TC37 | ⬜ Pending |

Full test plan: [TESTING.md](./TESTING.md)

## Requirements

- Python 3.9+
- pip

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

## Running tests

```bash
# all tests
pytest

# specific file
pytest tests/test_login.py

# headed mode (visible browser)
pytest --headed

# specific browser
pytest --browser firefox

# parallel execution
pytest -n auto
```

## License

[MIT](LICENSE)
