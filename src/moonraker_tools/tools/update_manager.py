"""Tools for interacting with the Moonraker update_manager API."""

from typing import Any, Dict, Optional

from ..client import MoonrakerClient


class UpdateManagerTools:
    """A class to encapsulate update_manager-related API endpoints."""

    def __init__(self, client: MoonrakerClient) -> None:
        """
        Initialize the UpdateManagerTools with a MoonrakerClient instance.

        Args:
            client: An instance of MoonrakerClient.
        """
        self._client = client

    async def get_status(self) -> Dict[str, Any]:
        """
        Get the update status.

        Returns:
            A dictionary containing the update status.
        """
        return await self._client.get("/machine/update/status")

    async def refresh(self, name: Optional[str] = None) -> Dict[str, Any]:
        """
        Refresh the update status.

        Args:
            name: The name of the software to refresh.

        Returns:
            A dictionary containing the updated status.
        """
        data = {}
        if name is not None:
            data["name"] = name
        return await self._client.post("/machine/update/refresh", data=data)

    async def upgrade(self, name: Optional[str] = None) -> str:
        """
        Upgrade the requested software.

        Args:
            name: The name of the software to upgrade.

        Returns:
            A string confirming the action.
        """
        data = {}
        if name is not None:
            data["name"] = name
        return await self._client.post("/machine/update/upgrade", data=data)

    async def recover(self, name: str, hard: bool = False) -> str:
        """
        Recover a corrupt repo.

        Args:
            name: The name of the software to recover.
            hard: Whether to perform a hard recovery.

        Returns:
            A string confirming the action.
        """
        data = {"name": name, "hard": hard}
        return await self._client.post("/machine/update/recover", data=data)

    async def rollback(self, name: str) -> str:
        """
        Rollback to the previous version.

        Args:
            name: The name of the software to rollback.

        Returns:
            A string confirming the action.
        """
        data = {"name": name}
        return await self._client.post("/machine/update/rollback", data=data)
