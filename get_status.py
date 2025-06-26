"""A script to get the status of a Moonraker instance."""

import asyncio
import os

from dotenv import load_dotenv
from moonraker_tools.client import MoonrakerClient
from moonraker_tools.tools.printer import PrinterTools

load_dotenv()


async def main() -> None:
    """Get the printer status."""
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        print("MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file.")
        return

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    printer_tools = PrinterTools(client)

    try:
        status = await printer_tools.get_info()
        print(status)
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
