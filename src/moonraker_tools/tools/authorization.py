"""Tools for interacting with the Moonraker authorization API."""

from typing import Any, Dict, List, Optional

from ..client import MoonrakerClient


class AuthorizationTools:
    """A class to encapsulate authorization-related API endpoints."""

    def __init__(self, client: MoonrakerClient) -> None:
        """
        Initialize the AuthorizationTools with a MoonrakerClient instance.

        Args:
            client: An instance of MoonrakerClient.
        """
        self._client = client

    async def login(
        self, username: str, password: str, source: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Log in a user.

        Args:
            username: The user's login name.
            password: The user's password.
            source: The authentication source.

        Returns:
            A dictionary containing the login token and user information.
        """
        data = {"username": username, "password": password}
        if source:
            data["source"] = source
        return await self._client.post("/access/login", data=data)

    async def logout(self) -> Dict[str, str]:
        """
        Log out the current user.

        Returns:
            A dictionary containing the username and a confirmation action.
        """
        return await self._client.post("/access/logout")

    async def get_current_user(self) -> Dict[str, Any]:
        """
        Get information about the currently logged-in user.

        Returns:
            A dictionary containing user information.
        """
        return await self._client.get("/access/user")

    async def create_user(self, username: str, password: str) -> Dict[str, Any]:
        """
        Create a new local user.

        Args:
            username: The new user's login name.
            password: The new user's password.

        Returns:
            A dictionary containing the new user's token and information.
        """
        data = {"username": username, "password": password}
        return await self._client.post("/access/user", data=data)

    async def delete_user(self, username: str) -> Dict[str, str]:
        """
        Delete a user.

        Args:
            username: The username of the user to delete.

        Returns:
            A dictionary containing the username and a confirmation action.
        """
        data = {"username": username}
        return await self._client.delete("/access/user", params=data)

    async def list_users(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        List all available users.

        Returns:
            A dictionary containing a list of users.
        """
        return await self._client.get("/access/users/list")

    async def reset_password(
        self, password: str, new_password: str
    ) -> Dict[str, str]:
        """
        Reset the current user's password.

        Args:
            password: The current password.
            new_password: The new password.

        Returns:
            A dictionary containing the username and a confirmation action.
        """
        data = {"password": password, "new_password": new_password}
        return await self._client.post("/access/user/password", data=data)

    async def refresh_jwt(self, refresh_token: str) -> Dict[str, Any]:
        """
        Refresh a JSON Web Token.

        Args:
            refresh_token: The refresh token.

        Returns:
            A dictionary containing the new access token.
        """
        data = {"refresh_token": refresh_token}
        return await self._client.post("/access/refresh_jwt", data=data)

    async def generate_oneshot_token(self) -> str:
        """
        Generate a one-shot token for temporary access.

        Returns:
            A string containing the one-shot token.
        """
        return await self._client.get("/access/oneshot_token")

    async def get_api_key(self) -> str:
        """
        Get the current API key.

        Returns:
            A string containing the API key.
        """
        return await self._client.get("/access/api_key")

    async def generate_api_key(self) -> str:
        """
        Generate a new API key.

        Returns:
            A string containing the new API key.
        """
        return await self._client.post("/access/api_key")
