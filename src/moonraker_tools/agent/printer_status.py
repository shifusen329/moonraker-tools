"""A tool for the AI agent to get the printer status."""

import os
from typing import Any, Dict

from ..client import MoonrakerClient
from ..tools.printer import PrinterTools


async def get_printer_status() -> Dict[str, Any]:
    """
    Get the current status of the printer.

    Returns:
        A dictionary containing the printer status.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    printer_tools = PrinterTools(client)

    try:
        status = await printer_tools.get_info()
    finally:
        await client.close()

    return status
