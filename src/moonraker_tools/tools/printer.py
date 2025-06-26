"""Tools for interacting with the Moonraker printer API."""

from typing import Any, Dict, List, Optional

from ..client import MoonrakerClient


class PrinterTools:
    """A class to encapsulate printer-related API endpoints."""

    def __init__(self, client: MoonrakerClient) -> None:
        """
        Initialize the PrinterTools with a MoonrakerClient instance.

        Args:
            client: An instance of MoonrakerClient.
        """
        self._client = client

    async def get_info(self) -> Dict[str, Any]:
        """
        Get Klippy host information.

        Returns:
            A dictionary containing Klippy's state and host information.
        """
        return await self._client.get("/printer/info")

    async def emergency_stop(self) -> str:
        """
        Issue an emergency stop to the printer.

        Returns:
            A string confirming the action.
        """
        return await self._client.post("/printer/emergency_stop")

    async def restart(self) -> str:
        """
        Request a Klipper "soft" restart.

        Returns:
            A string confirming the action.
        """
        return await self._client.post("/printer/restart")

    async def firmware_restart(self) -> str:
        """
        Request a complete Klipper restart.

        Returns:
            A string confirming the action.
        """
        return await self._client.post("/printer/firmware_restart")

    async def list_objects(self) -> Dict[str, List[str]]:
        """
        List loaded printer objects.

        Returns:
            A dictionary containing a list of printer objects.
        """
        return await self._client.get("/printer/objects/list")

    async def query_objects(self, objects: Dict[str, Any]) -> Dict[str, Any]:
        """
        Query the status of a provided set of printer objects.

        Args:
            objects: A dictionary of printer objects to query.

        Returns:
            A dictionary containing the status of the requested objects.
        """
        data = {"objects": objects}
        return await self._client.post("/printer/objects/query", data=data)

    async def run_gcode_script(self, script: str) -> str:
        """
        Execute a gcode script.

        Args:
            script: The gcode script to execute.

        Returns:
            A string confirming the action.
        """
        data = {"script": script}
        return await self._client.post("/printer/gcode/script", data=data)

    async def start_print(self, filename: str) -> str:
        """
        Start a print job.

        Args:
            filename: The name of the gcode file to print.

        Returns:
            A string confirming the action.
        """
        params = {"filename": filename}
        return await self._client.post("/printer/print/start", data=params)

    async def pause_print(self) -> str:
        """
        Pause a print job.

        Returns:
            A string confirming the action.
        """
        return await self._client.post("/printer/print/pause")

    async def resume_print(self) -> str:
        """
        Resume a print job.

        Returns:
            A string confirming the action.
        """
        return await self._client.post("/printer/print/resume")

    async def cancel_print(self) -> str:
        """
        Cancel a print job.

        Returns:
            A string confirming the action.
        """
        return await self._client.post("/printer/print/cancel")
