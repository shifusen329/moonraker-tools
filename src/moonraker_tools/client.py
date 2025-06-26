"""A client for interacting with the Moonraker API."""

from typing import Any, Dict, Optional

import httpx


class MoonrakerClient:
    """A client for interacting with the Moonraker API."""

    def __init__(
        self,
        host: str,
        port: int = 7125,
        api_key: Optional[str] = None,
    ) -> None:
        """
        Initialize the MoonrakerClient.

        Args:
            host: The hostname or IP address of the Moonraker instance.
            port: The port number for the Moonraker API.
            api_key: The API key for authentication, if required.
        """
        self.base_url = f"http://{host}:{port}"
        self.api_key = api_key
        self._client = httpx.AsyncClient(base_url=self.base_url)

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """
        Send a GET request to a Moonraker API endpoint.

        Args:
            endpoint: The API endpoint to request.
            params: Optional dictionary of query parameters.

        Returns:
            The JSON response from the API.
        """
        headers = self._get_headers()
        response = await self._client.get(endpoint, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    async def post(
        self, endpoint: str, data: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Send a POST request to a Moonraker API endpoint.

        Args:
            endpoint: The API endpoint to request.
            data: Optional dictionary of data to send in the request body.

        Returns:
            The JSON response from the API.
        """
        headers = self._get_headers()
        response = await self._client.post(endpoint, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    async def delete(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Send a DELETE request to a Moonraker API endpoint.

        Args:
            endpoint: The API endpoint to request.
            params: Optional dictionary of query parameters.

        Returns:
            The JSON response from the API.
        """
        headers = self._get_headers()
        response = await self._client.delete(endpoint, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    def _get_headers(self) -> Dict[str, str]:
        """
        Get the headers for the request, including the API key if available.

        Returns:
            A dictionary of headers.
        """
        headers = {}
        if self.api_key:
            headers["X-Api-Key"] = self.api_key
        return headers

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()
