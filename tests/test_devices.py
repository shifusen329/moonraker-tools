"""Tests for the devices tools."""

from typing import Any, Dict, Generator, List
from unittest.mock import AsyncMock, patch

import pytest
from moonraker_tools.client import MoonrakerClient
from moonraker_tools.tools.devices import DevicesTools


@pytest.fixture
def mock_client() -> Generator[AsyncMock, None, None]:
    """Fixture for a mocked MoonrakerClient."""
    with patch("moonraker_tools.client.MoonrakerClient", autospec=True) as mock:
        yield mock


@pytest.fixture
def devices_tools(mock_client: AsyncMock) -> DevicesTools:
    """Fixture for DevicesTools with a mocked client."""
    return DevicesTools(mock_client)


@pytest.mark.asyncio
async def test_get_device_list(
    devices_tools: DevicesTools, mock_client: AsyncMock
) -> None:
    """Test getting the device list."""
    # Arrange
    mock_response: Dict[str, List[Dict[str, Any]]] = {
        "devices": [
            {
                "device": "green_led",
                "status": "off",
                "locked_while_printing": True,
                "type": "gpio",
            }
        ]
    }
    mock_client.get.return_value = mock_response

    # Act
    result = await devices_tools.get_device_list()

    # Assert
    mock_client.get.assert_called_once_with("/machine/device_power/devices")
    assert result == mock_response
