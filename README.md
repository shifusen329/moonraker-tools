# Moonraker Tools

A Python client for the Moonraker API, designed for AI agents.

## Installation

To install the project and its dependencies, you can use `uv`. It is recommended to use a virtual environment.

```bash
uv venv
source .venv/bin/activate
uv pip install -e .[dev]
```

## Usage

The library provides a `MoonrakerClient` to interact with the Moonraker API. You can use it as follows:

```python
import asyncio
from moonraker_tools.client import MoonrakerClient

async def main():
    client = MoonrakerClient(host="your_printer_ip")
    try:
        info = await client.get("/printer/info")
        print(info)
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## Running Tests

To run the unit tests:

```bash
uv run pytest
```

To run the integration tests, you need to create a `.env` file with your printer's connection details:

```
MOONRAKER_HOST=your_printer_ip
MOONRAKER_PORT=7125
MOONRAKER_API_KEY=
```

Then run the integration tests:

```bash
uv run pytest tests/test_integration.py
```

## Agent Tools

This project also includes a set of higher-level agent tools that can be used by an AI agent to manage the printer. These tools are located in the `src/moonraker_tools/agent` directory.

Example usage:

```python
import asyncio
from moonraker_tools.agent.printer_status import get_printer_status

async def main():
    status = await get_printer_status()
    print(status)

if __name__ == "__main__":
    asyncio.run(main())
