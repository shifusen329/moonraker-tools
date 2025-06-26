"""Integration tests for the Moonraker client."""

import os

import pytest
from dotenv import load_dotenv
from moonraker_tools.client import MoonrakerClient

load_dotenv()


@pytest.mark.asyncio
async def test_connection() -> None:
    """Test the connection to the Moonraker instance."""
    # Arrange
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    assert host, "MOONRAKER_HOST is not set"
    assert port, "MOONRAKER_PORT is not set"

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)

    # Act
    try:
        response = await client.get("/server/info")
    finally:
        await client.close()

    # Assert
    assert response is not None
    assert "result" in response
    assert "klippy_connected" in response["result"]
