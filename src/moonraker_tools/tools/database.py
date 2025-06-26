"""Tools for interacting with the Moonraker database API."""

from typing import Any, Dict, List, Optional, Union

from ..client import MoonrakerClient


class DatabaseTools:
    """A class to encapsulate database-related API endpoints."""

    def __init__(self, client: MoonrakerClient) -> None:
        """
        Initialize the DatabaseTools with a MoonrakerClient instance.

        Args:
            client: An instance of MoonrakerClient.
        """
        self._client = client

    async def list_namespaces(self) -> Dict[str, List[str]]:
        """
        List all namespaces with read and/or write access.

        Returns:
            A dictionary containing a list of namespaces.
        """
        return await self._client.get("/server/database/list")

    async def get_item(
        self, namespace: str, key: Optional[Union[str, List[str]]] = None
    ) -> Dict[str, Any]:
        """
        Retrieve an item from a specified namespace.

        Args:
            namespace: The namespace of the item to retrieve.
            key: The key indicating the field or fields within the namespace to retrieve.

        Returns:
            A dictionary containing the requested item.
        """
        params = {"namespace": namespace}
        if key is not None:
            params["key"] = key
        return await self._client.get("/server/database/item", params=params)

    async def add_item(
        self, namespace: str, key: Union[str, List[str]], value: Any
    ) -> Dict[str, Any]:
        """
        Insert an item into the database.

        Args:
            namespace: The namespace where the value should be inserted.
            key: The key indicating the field or fields where the value should be inserted.
            value: The value to insert in the database.

        Returns:
            A dictionary containing the inserted item.
        """
        data = {"namespace": namespace, "key": key, "value": value}
        return await self._client.post("/server/database/item", data=data)

    async def delete_item(
        self, namespace: str, key: Union[str, List[str]]
    ) -> Dict[str, Any]:
        """
        Delete an item from a namespace at the specified key.

        Args:
            namespace: The namespace where the item should be removed.
            key: The key indicating the field or fields where the item should be removed.

        Returns:
            A dictionary containing the removed item.
        """
        params = {"namespace": namespace, "key": key}
        return await self._client.delete("/server/database/item", params=params)
