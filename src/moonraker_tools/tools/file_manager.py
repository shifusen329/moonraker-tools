"""Tools for interacting with the Moonraker file_manager API."""

from typing import Any, Dict, List, Optional

from ..client import MoonrakerClient


class FileManagerTools:
    """A class to encapsulate file_manager-related API endpoints."""

    def __init__(self, client: MoonrakerClient) -> None:
        """
        Initialize the FileManagerTools with a MoonrakerClient instance.

        Args:
            client: An instance of MoonrakerClient.
        """
        self._client = client

    async def list_files(self, root: str = "gcodes") -> List[Dict[str, Any]]:
        """
        List available files in a root.

        Args:
            root: The root to list files from.

        Returns:
            A list of file information dictionaries.
        """
        params = {"root": root}
        return await self._client.get("/server/files/list", params=params)

    async def get_directory_info(
        self, path: str = "gcodes", extended: bool = False
    ) -> Dict[str, Any]:
        """
        Get information about a directory.

        Args:
            path: The path to the directory.
            extended: Whether to include extended metadata for gcode files.

        Returns:
            A dictionary containing directory information.
        """
        params = {"path": path, "extended": extended}
        return await self._client.get("/server/files/directory", params=params)

    async def create_directory(self, path: str) -> Dict[str, Any]:
        """
        Create a directory.

        Args:
            path: The path to the directory to create.

        Returns:
            A dictionary containing information about the created directory.
        """
        data = {"path": path}
        return await self._client.post("/server/files/directory", data=data)

    async def delete_directory(self, path: str, force: bool = False) -> Dict[str, Any]:
        """
        Delete a directory.

        Args:
            path: The path to the directory to delete.
            force: Whether to force delete the directory and its contents.

        Returns:
            A dictionary containing information about the deleted directory.
        """
        params = {"path": path, "force": force}
        return await self._client.delete("/server/files/directory", params=params)

    async def move_item(self, source: str, dest: str) -> Dict[str, Any]:
        """
        Move a file or directory.

        Args:
            source: The source path.
            dest: The destination path.

        Returns:
            A dictionary containing information about the moved item.
        """
        data = {"source": source, "dest": dest}
        return await self._client.post("/server/files/move", data=data)

    async def copy_item(self, source: str, dest: str) -> Dict[str, Any]:
        """
        Copy a file or directory.

        Args:
            source: The source path.
            dest: The destination path.

        Returns:
            A dictionary containing information about the copied item.
        """
        data = {"source": source, "dest": dest}
        return await self._client.post("/server/files/copy", data=data)

    async def delete_file(self, path: str) -> Dict[str, Any]:
        """
        Delete a file.

        Args:
            path: The path to the file to delete.

        Returns:
            A dictionary containing information about the deleted file.
        """
        return await self._client.delete(f"/server/files/{path}")
