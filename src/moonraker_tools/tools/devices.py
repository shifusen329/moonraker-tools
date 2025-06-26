"""Tools for interacting with the Moonraker devices API."""

from typing import Any, Dict, List

from ..client import MoonrakerClient


class DevicesTools:
    """A class to encapsulate devices-related API endpoints."""

    def __init__(self, client: MoonrakerClient) -> None:
        """
        Initialize the DevicesTools with a MoonrakerClient instance.

        Args:
            client: An instance of MoonrakerClient.
        """
        self._client = client

    async def get_device_list(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Get the list of power devices.

        Returns:
            A dictionary containing a list of power devices.
        """
        return await self._client.get("/machine/device_power/devices")

    async def get_device_state(self, device: str) -> Dict[str, str]:
        """
        Get the state of a single power device.

        Args:
            device: The name of the device.

        Returns:
            A dictionary containing the device name and its state.
        """
        params = {"device": device}
        return await self._client.get("/machine/device_power/device", params=params)

    async def set_device_state(self, device: str, action: str) -> Dict[str, str]:
        """
        Set the state of a single power device.

        Args:
            device: The name of the device.
            action: The action to perform (on, off, toggle).

        Returns:
            A dictionary containing the device name and its new state.
        """
        data = {"device": device, "action": action}
        return await self._client.post("/machine/device_power/device", data=data)

    async def get_batch_device_status(
        self, devices: List[str]
    ) -> Dict[str, str]:
        """
        Get the status of multiple power devices.

        Args:
            devices: A list of device names.

        Returns:
            A dictionary containing device names and their states.
        """
        params = {device: None for device in devices}
        return await self._client.get("/machine/device_power/status", params=params)

    async def batch_power_on(self, devices: List[str]) -> Dict[str, str]:
        """
        Power on multiple devices.

        Args:
            devices: A list of device names.

        Returns:
            A dictionary containing device names and their new states.
        """
        data = {device: None for device in devices}
        return await self._client.post("/machine/device_power/on", data=data)

    async def batch_power_off(self, devices: List[str]) -> Dict[str, str]:
        """
        Power off multiple devices.

        Args:
            devices: A list of device names.

        Returns:
            A dictionary containing device names and their new states.
        """
        data = {device: None for device in devices}
        return await self._client.post("/machine/device_power/off", data=data)
