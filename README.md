# Azure Speech to Text Example

This example demonstrates how to use the Azure Speech to
transcribe mp4 files to text.

## Prerequisites
- Azure account
- Azure Speech to Text API key
- Python 3.12 or later
  - Recommended:
    [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)
  - `pyenv install 3.12`
  - `pyenv local 3.12`
- Poetry (https://python-poetry.org/)

## Dev Setup

- `poetry install`
- `pre-commit install`
- cp .env.example .env
  - Fill in the .env file with your Azure Speech to Text API key


## VSCode Extensions

There are a few recommended [vscode extensions](./.vscode/extensions.json) for
this project. vscode will prompt you to install them when you open the project.
You can also install them manually by pressing Cmd+Shift+P and typing
`Show Recommended Extensions`.


## Running the sample

```bash
python -m speech2text.main -f <path-to-mp4-file> -l <language>
```

Example:

```bash
python -m speech2text.main -f "/tmp/sample.mp4" -l "en-US"
```
