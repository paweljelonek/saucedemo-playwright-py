# saucedemo-playwright-py

> ℹ️ **Why does this repo exist?**
>
> The real test suites are locked behind NDAs - which is great for clients, less great for anyone
> trying to verify I actually know what I'm doing.
> Enter SauceDemo: a site built to be tested, with credentials in the docs and no production data at risk.
> Same approach, same patterns - just without the legal paperwork.

---

Automated end-to-end tests for [saucedemo.com](https://www.saucedemo.com) built with [Playwright](https://playwright.dev/python/) and [pytest](https://pytest.org), following the Page Object Model pattern.

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
