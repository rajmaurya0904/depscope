# Depscope

**Scans project dependencies to generate a lightweight architecture dependency matrix and detects unwanted circular layer violations.**

Large Python codebases slowly rot as modules quietly import across layer boundaries and tangled circular dependencies make refactoring agonizing. Depscope inspects your import statements statically to map module relationships, flagging forbidden layer leaks and cycle loops before they harden into permanent technical debt.

## Example

<!-- A real command and its REAL pasted output. Run it first. -->

## Installation

```bash
pip install depscope
```

For development or editable install:

```bash
pip install -e ".[dev]"
```

## Usage

<!-- The 2-4 commands people actually need, one line each. -->

## How it works

- Parses Python files to collect import statements.
- Builds a directed graph of module dependencies.
- Detects forbidden layer violations and cycles in the graph.
- Exports the dependency matrix and cycle report as CSV files.

## Limitations

- Only analyzes static import statements; dynamic imports (e.g., `importlib.import_module`) are ignored.
- Works only on packages present in the current environment; it cannot resolve missing or external dependencies.
- Does not process namespace packages or modules loaded from zip files.
- Scans files within the project directory only; external libraries are excluded.

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
