"""Tools for interacting with the Moonraker server API."""

from typing import Any, Dict, List, Optional

from ..client import MoonrakerClient


class ServerTools:
    """A class to encapsulate server-related API endpoints."""

    def __init__(self, client: MoonrakerClient) -> None:
        """
        Initialize the ServerTools with a MoonrakerClient instance.

        Args:
            client: An instance of MoonrakerClient.
        """
        self._client = client

    async def get_info(self) -> Dict[str, Any]:
        """
        Get server information.

        Returns:
            A dictionary containing server information.
        """
        return await self._client.get("/server/info")

    async def get_config(self) -> Dict[str, Any]:
        """
        Get the server configuration.

        Returns:
            A dictionary containing the server configuration.
        """
        return await self._client.get("/server/config")

    async def get_temperature_store(
        self, include_monitors: bool = False
    ) -> Dict[str, Any]:
        """
        Get cached temperature data.

        Args:
            include_monitors: Whether to include temperature monitors.

        Returns:
            A dictionary containing temperature data.
        """
        params = {"include_monitors": include_monitors}
        return await self._client.get("/server/temperature_store", params=params)

    async def get_gcode_store(self, count: Optional[int] = None) -> Dict[str, Any]:
        """
        Get cached gcode responses.

        Args:
            count: The number of responses to return.

        Returns:
            A dictionary containing gcode responses.
        """
        params: Dict[str, Any] = {}
        if count is not None:
            params["count"] = count
        return await self._client.get("/server/gcode_store", params=params)

    async def restart(self) -> str:
        """
        Restart the server.

        Returns:
            A string confirming the action.
        """
        return await self._client.post("/server/restart")
