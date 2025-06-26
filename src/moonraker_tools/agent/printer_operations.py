"""Agent tools for interacting with the Moonraker printer API."""

import os
from typing import Any, Dict, List

from ..client import MoonrakerClient
from ..tools.printer import PrinterTools


async def emergency_stop() -> str:
    """
    Issue an emergency stop to the printer.

    Returns:
        A string confirming the action.
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
        result = await printer_tools.emergency_stop()
    finally:
        await client.close()

    return result


async def restart() -> str:
    """
    Request a Klipper "soft" restart.

    Returns:
        A string confirming the action.
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
        result = await printer_tools.restart()
    finally:
        await client.close()

    return result


async def firmware_restart() -> str:
    """
    Request a complete Klipper restart.

    Returns:
        A string confirming the action.
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
        result = await printer_tools.firmware_restart()
    finally:
        await client.close()

    return result


async def list_objects() -> Dict[str, List[str]]:
    """
    List loaded printer objects.

    Returns:
        A dictionary containing a list of printer objects.
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
        result = await printer_tools.list_objects()
    finally:
        await client.close()

    return result


async def query_objects(objects: Dict[str, Any]) -> Dict[str, Any]:
    """
    Query the status of a provided set of printer objects.

    Args:
        objects: A dictionary of printer objects to query.

    Returns:
        A dictionary containing the status of the requested objects.
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
        result = await printer_tools.query_objects(objects)
    finally:
        await client.close()

    return result


async def run_gcode_script(script: str) -> str:
    """
    Execute a gcode script.

    Args:
        script: The gcode script to execute.

    Returns:
        A string confirming the action.
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
        result = await printer_tools.run_gcode_script(script)
    finally:
        await client.close()

    return result


async def start_print(filename: str) -> str:
    """
    Start a print job.

    Args:
        filename: The name of the gcode file to print.

    Returns:
        A string confirming the action.
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
        result = await printer_tools.start_print(filename)
    finally:
        await client.close()

    return result


async def pause_print() -> str:
    """
    Pause a print job.

    Returns:
        A string confirming the action.
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
        result = await printer_tools.pause_print()
    finally:
        await client.close()

    return result


async def resume_print() -> str:
    """
    Resume a print job.

    Returns:
        A string confirming the action.
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
        result = await printer_tools.resume_print()
    finally:
        await client.close()

    return result


async def cancel_print() -> str:
    """
    Cancel a print job.

    Returns:
        A string confirming the action.
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
        result = await printer_tools.cancel_print()
    finally:
        await client.close()

    return result
