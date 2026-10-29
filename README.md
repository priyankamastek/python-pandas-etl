# python-pandas-etl

Python and pandas ETL exercises for Session 3.

## Requirements

- Python 3.14 or later (the version is set in `.python-version`)
- [uv](https://docs.astral.sh/uv/) (optional, but recommended)

## Project structure

```
python-pandas-etl/
├── pyproject.toml        # Project metadata and dependencies
├── uv.lock               # Locked dependency versions (used by uv)
├── .python-version       # Python version for this project
└── src/
    └── foundation/
        └── functions.py  # Example script
```

---

## Option 1: Run with uv (recommended)

`uv run` uses the project's `.venv` automatically, so you don't need to activate it.

### 1. Open the project folder

```cmd
cd /d "D:\July-Dec26\Business_Ask\CarGuru_Sep26\ILT_Sessions\Session3\python-pandas-etl"
```

### 2. Set up the environment (run once, and again after dependencies change)

```cmd
uv sync
```

This creates `.venv`, installs the Python version listed in `.python-version`, and installs the dependencies listed in `uv.lock`.

### 3. Run a Python file

```cmd
uv run python src\foundation\functions.py
```

or, more briefly:

```cmd
uv run src\foundation\functions.py
```

or run it as a module (use dots instead of slashes, and no `.py`):

```cmd
uv run python -m src.foundation.functions
```

Run this from the project root folder so Python can find the `src` package.

### 4. Run only one function

Use `python -c` to import a single function and call it:

```cmd
uv run python -c "from src.foundation.functions import validate_password; print(validate_password('hgtr@8uyt'))"
```

Output:

```
True
```

Change the value inside `validate_password('...')` to test a different password. In CMD, keep double quotes around the whole command and single quotes inside it.

This works because the test calls in `functions.py` sit under `if __name__ == "__main__":`, so they run only when you run the whole file, not when you import it.

### Useful uv commands

| Task | Command |
|---|---|
| Add a package | `uv add <package>` (e.g. `uv add pandas`) |
| Remove a package | `uv remove <package>` |
| List installed packages | `uv pip list` |
| Open a Python shell in the project env | `uv run python` |

---

## Option 2: Run without uv (standard Python + pip)

### 1. Open the project folder

```cmd
cd /d "D:\July-Dec26\Business_Ask\CarGuru_Sep26\ILT_Sessions\Session3\python-pandas-etl"
```

### 2. Create a virtual environment (run once)

```cmd
python -m venv .venv
```

### 3. Activate the virtual environment

CMD:

```cmd
.venv\Scripts\activate
```

PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

When the environment is active, `(.venv)` appears at the start of the prompt.

### 4. Install dependencies (run once)

```cmd
pip install pandas
```

### 5. Run a Python file

```cmd
python src\foundation\functions.py
```

To run only one function:

```cmd
python -c "from src.foundation.functions import validate_password; print(validate_password('hgtr@8uyt'))"
```

### 6. Deactivate when finished

```cmd
deactivate
```

---

## Expected output

Running the whole file (`src\foundation\functions.py`) prints:

```
['Alan', 'Turing']
alan.turing@techcompany.com
Is the password valid?  True
```
