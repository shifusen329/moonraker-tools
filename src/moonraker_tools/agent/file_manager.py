"""Agent tools for interacting with the Moonraker file_manager API."""

import os
from typing import Any, Dict, List

from ..client import MoonrakerClient
from ..tools.file_manager import FileManagerTools


async def list_files(root: str = "gcodes") -> List[Dict[str, Any]]:
    """
    List available files in a root.

    Args:
        root: The root to list files from.

    Returns:
        A list of file information dictionaries.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    file_manager_tools = FileManagerTools(client)

    try:
        files = await file_manager_tools.list_files(root=root)
    finally:
        await client.close()

    return files


async def get_directory_info(
    path: str = "gcodes", extended: bool = False
) -> Dict[str, Any]:
    """
    Get information about a directory.

    Args:
        path: The path to the directory.
        extended: Whether to include extended metadata for gcode files.

    Returns:
        A dictionary containing directory information.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    file_manager_tools = FileManagerTools(client)

    try:
        info = await file_manager_tools.get_directory_info(path=path, extended=extended)
    finally:
        await client.close()

    return info


async def create_directory(path: str) -> Dict[str, Any]:
    """
    Create a directory.

    Args:
        path: The path to the directory to create.

    Returns:
        A dictionary containing information about the created directory.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    file_manager_tools = FileManagerTools(client)

    try:
        result = await file_manager_tools.create_directory(path=path)
    finally:
        await client.close()

    return result


async def delete_directory(path: str, force: bool = False) -> Dict[str, Any]:
    """
    Delete a directory.

    Args:
        path: The path to the directory to delete.
        force: Whether to force delete the directory and its contents.

    Returns:
        A dictionary containing information about the deleted directory.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    file_manager_tools = FileManagerTools(client)

    try:
        result = await file_manager_tools.delete_directory(path=path, force=force)
    finally:
        await client.close()

    return result


async def move_item(source: str, dest: str) -> Dict[str, Any]:
    """
    Move a file or directory.

    Args:
        source: The source path.
        dest: The destination path.

    Returns:
        A dictionary containing information about the moved item.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    file_manager_tools = FileManagerTools(client)

    try:
        result = await file_manager_tools.move_item(source=source, dest=dest)
    finally:
        await client.close()

    return result


async def copy_item(source: str, dest: str) -> Dict[str, Any]:
    """
    Copy a file or directory.

    Args:
        source: The source path.
        dest: The destination path.

    Returns:
        A dictionary containing information about the copied item.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    file_manager_tools = FileManagerTools(client)

    try:
        result = await file_manager_tools.copy_item(source=source, dest=dest)
    finally:
        await client.close()

    return result


async def delete_file(path: str) -> Dict[str, Any]:
    """
    Delete a file.

    Args:
        path: The path to the file to delete.

    Returns:
        A dictionary containing information about the deleted file.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    file_manager_tools = FileManagerTools(client)

    try:
        result = await file_manager_tools.delete_file(path=path)
    finally:
        await client.close()

    return result
