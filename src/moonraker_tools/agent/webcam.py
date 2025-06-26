"""Agent tools for interacting with webcams."""

import os
from typing import Any, Dict, List, Optional

import httpx

from ..client import MoonrakerClient
from ..tools.webcams import WebcamsTools


async def download_snapshot(
    webcam_name: Optional[str] = None, output_path: str = "snapshot.jpg"
) -> str:
    """
    Downloads a snapshot from a configured webcam.

    Args:
        webcam_name: The name of the webcam to use. If None, the first available
                     webcam will be used.
        output_path: The path to save the snapshot image.

    Returns:
        The path where the snapshot was saved.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    webcams_tools = WebcamsTools(client)

    try:
        webcams_response = await webcams_tools.list_webcams()
        webcams = webcams_response.get("result", {}).get("webcams", [])

        if not webcams:
            raise RuntimeError("No webcams found.")

        target_webcam = None
        if webcam_name:
            for cam in webcams:
                if cam.get("name") == webcam_name:
                    target_webcam = cam
                    break
            if not target_webcam:
                raise ValueError(f"Webcam '{webcam_name}' not found.")
        else:
            # Default to the first webcam
            target_webcam = webcams[0]

        snapshot_url = target_webcam.get("snapshot_url")
        if not snapshot_url:
            raise ValueError(
                f"Webcam '{target_webcam.get('name')}' does not have a snapshot URL."
            )

        # If the URL is relative, prepend the base URL
        if snapshot_url.startswith("/"):
            snapshot_url = f"{client.base_url}{snapshot_url}"

        async with httpx.AsyncClient() as snapshot_client:
            response = await snapshot_client.get(snapshot_url)
            response.raise_for_status()

        with open(output_path, "wb") as f:
            f.write(response.content)

    finally:
        await client.close()

    return output_path
