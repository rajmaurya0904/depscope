# Depscope

**Scans project dependencies to generate a lightweight architecture dependency matrix and detects unwanted circular layer violations.**

Large Python codebases slowly rot as modules quietly import across layer boundaries and tangled circular dependencies make refactoring agonizing. Depscope inspects your import statements statically to map module relationships, flagging forbidden layer leaks and cycle loops before they harden into permanent technical debt.

## Example

<!-- A real command and its REAL pasted output. Run it first. -->

## Install

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

<!-- Honest and short: what it does NOT do, known gaps. -->

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
