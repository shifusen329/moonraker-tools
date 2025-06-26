"""Tools for interacting with the Moonraker webcams API."""

from typing import Any, Dict, List, Optional

from ..client import MoonrakerClient


class WebcamsTools:
    """A class to encapsulate webcams-related API endpoints."""

    def __init__(self, client: MoonrakerClient) -> None:
        """
        Initialize the WebcamsTools with a MoonrakerClient instance.

        Args:
            client: An instance of MoonrakerClient.
        """
        self._client = client

    async def list_webcams(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        List all webcams.

        Returns:
            A dictionary containing a list of webcams.
        """
        return await self._client.get("/server/webcams/list")

    async def get_webcam_info(self, uid: str) -> Dict[str, Any]:
        """
        Get information about a single webcam.

        Args:
            uid: The unique ID of the webcam.

        Returns:
            A dictionary containing webcam information.
        """
        params = {"uid": uid}
        return await self._client.get("/server/webcams/item", params=params)

    async def add_or_update_webcam(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Add or update a webcam.

        Args:
            **kwargs: The webcam parameters.

        Returns:
            A dictionary containing the new or updated webcam information.
        """
        return await self._client.post("/server/webcams/item", data=kwargs)

    async def delete_webcam(self, uid: str) -> Dict[str, Any]:
        """
        Delete a webcam.

        Args:
            uid: The unique ID of the webcam to delete.

        Returns:
            A dictionary containing the deleted webcam information.
        """
        params = {"uid": uid}
        return await self._client.delete("/server/webcams/item", params=params)

    async def test_webcam(self, uid: str) -> Dict[str, Any]:
        """
        Test a webcam.

        Args:
            uid: The unique ID of the webcam to test.

        Returns:
            A dictionary containing the test results.
        """
        params = {"uid": uid}
        return await self._client.post("/server/webcams/test", data=params)
