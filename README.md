# Crazy-Calculator 🚀

A compact Python project with multiple calculator implementations, a small Flask wiring, and unit tests. This README gives a concise, friendly introduction and shows how to set up a development environment on Windows (cmd.exe), install dependencies, run the app, and run tests.

## Project overview

Crazy-Calculator contains modular calculator implementations and minimal app wiring to expose or test them. It's intended to be easy to run locally and extend.

Key items in this repository:

- `requirements.txt` — project dependencies.
- `run.py` — top-level entrypoint script (run this to start the app if it's the intended runner).
- `src/` — application source code:
  - `calculators/` — calculator implementations (`calculator_1.py`, `calculator_2.py`, `calculator_3.py`, `calculator_4.py`).
  - `drivers/` — driver utilities (for example `numpy_handler.py`).
  - `interfaces/` — driver interfaces (for example `driver_handler_interface.py`).
  - `errors/` — custom error classes and error controller (for example `error_controller.py`, `http_bad_request.py`, `http_unprocessable_entity.py`).
  - `main/` — app wiring, factories and routes (`factories/`, `routes/`, `server/`).
- `tests/` — unit tests for the calculator modules (for example `calculator_1_test.py` … `calculator_4_test.py`).

## Quick start (Windows — cmd.exe) ⚙️

These commands assume you have Python installed and available on your PATH. They are intended for the Windows Command Prompt (cmd.exe).

1) Create a virtual environment in the repository root (recommended name: `.venv`):

```cmd
python -m venv .venv
```

2) Activate the virtual environment:

```cmd
.venv\Scripts\activate
```

3) (Optional) Upgrade pip inside the venv:

```cmd
python -m pip install --upgrade pip
```

4) Install dependencies from `requirements.txt`:

```cmd
pip install -r requirements.txt
```

5) Run the app (if `run.py` is the entrypoint):

```cmd
python run.py
```

If the project boots a Flask app from `src/main/server/server.py`, you can open that file to see the exact run command or configuration (host/port). Adjust as needed.

## Docker / Docker Compose 🐳

This repository now includes a `docker-compose.yml` file that allows you to run the application in containers using Docker Compose.

Basic instructions (with Docker Desktop running):

```cmd
docker compose up --build -d
```

- View logs:

```cmd
docker compose logs -f
```

- Stop and remove containers/networks created by Compose:

```cmd
docker compose down
```

If you're using the older Compose v1, replace `docker compose` with `docker-compose` in the commands above.

If you prefer to run the application locally without Docker, follow the "Quick start" section above.

## Running tests 🧪

If `pytest` is available (it may already be in `requirements.txt`), run the test suite with:

```cmd
python -m pytest -q
```

If `pytest` isn't installed, install it inside the active virtualenv first:

```cmd
pip install pytest
python -m pytest -q
```

## Tips & troubleshooting ⚠️

- If you see import errors, ensure the virtualenv is activated and dependencies are installed.
- If the server doesn't start, open `src/main/server/server.py` and `run.py` to confirm how the Flask app is created and run.
- To add or update dependencies, edit `requirements.txt` and re-run `pip install -r requirements.txt`.

## Contributing & next steps ✨

If you'd like the README to include API examples (sample request/response payloads), exact server run options, or a short development checklist, tell me what you prefer and I will add it.

Enjoy exploring the project! 🧠✨
