"""Tools for interacting with the Moonraker machine API."""

from typing import Any, Dict, Optional

from ..client import MoonrakerClient


class MachineTools:
    """A class to encapsulate machine-related API endpoints."""

    def __init__(self, client: MoonrakerClient) -> None:
        """
        Initialize the MachineTools with a MoonrakerClient instance.

        Args:
            client: An instance of MoonrakerClient.
        """
        self._client = client

    async def get_system_info(self) -> Dict[str, Any]:
        """
        Get system information.

        Returns:
            A dictionary containing system information.
        """
        return await self._client.get("/machine/system_info")

    async def shutdown(self) -> str:
        """
        Shutdown the operating system.

        Returns:
            A string confirming the action.
        """
        return await self._client.post("/machine/shutdown")

    async def reboot(self) -> str:
        """
        Reboot the operating system.

        Returns:
            A string confirming the action.
        """
        return await self._client.post("/machine/reboot")

    async def restart_service(self, service: str) -> str:
        """
        Restart a system service.

        Args:
            service: The name of the service to restart.

        Returns:
            A string confirming the action.
        """
        data = {"service": service}
        return await self._client.post("/machine/services/restart", data=data)

    async def stop_service(self, service: str) -> str:
        """
        Stop a system service.

        Args:
            service: The name of the service to stop.

        Returns:
            A string confirming the action.
        """
        data = {"service": service}
        return await self._client.post("/machine/services/stop", data=data)

    async def start_service(self, service: str) -> str:
        """
        Start a system service.

        Args:
            service: The name of the service to start.

        Returns:
            A string confirming the action.
        """
        data = {"service": service}
        return await self._client.post("/machine/services/start", data=data)

    async def get_proc_stats(self) -> Dict[str, Any]:
        """
        Get process statistics.

        Returns:
            A dictionary containing process statistics.
        """
        return await self._client.get("/machine/proc_stats")

    async def get_sudo_info(self, check_access: bool = False) -> Dict[str, Any]:
        """
        Get sudo information.

        Args:
            check_access: Whether to check for sudo access.

        Returns:
            A dictionary containing sudo information.
        """
        params = {"check_access": check_access}
        return await self._client.get("/machine/sudo/info", params=params)

    async def set_sudo_password(self, password: str) -> Dict[str, Any]:
        """
        Set the sudo password.

        Args:
            password: The sudo password.

        Returns:
            A dictionary containing the sudo responses.
        """
        data = {"password": password}
        return await self._client.post("/machine/sudo/password", data=data)
