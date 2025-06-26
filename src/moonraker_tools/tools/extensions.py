"""Tools for interacting with the Moonraker extensions API."""

from typing import Any, Dict, List, Optional, Union

from ..client import MoonrakerClient


class ExtensionsTools:
    """A class to encapsulate extensions-related API endpoints."""

    def __init__(self, client: MoonrakerClient) -> None:
        """
        Initialize the ExtensionsTools with a MoonrakerClient instance.

        Args:
            client: An instance of MoonrakerClient.
        """
        self._client = client

    async def list_extensions(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        List all available extensions.

        Returns:
            A dictionary containing a list of agents.
        """
        return await self._client.get("/server/extensions/list")

    async def call_extension_method(
        self,
        agent: str,
        method: str,
        arguments: Optional[Union[List[Any], Dict[str, Any]]] = None,
    ) -> Any:
        """
        Call a method on a connected agent.

        Args:
            agent: The name of the registered agent.
            method: The name of the method to call.
            arguments: The arguments to send with the method.

        Returns:
            The result received from the agent.
        """
        data = {"agent": agent, "method": method}
        if arguments is not None:
            data["arguments"] = arguments
        return await self._client.post("/server/extensions/request", data=data)
