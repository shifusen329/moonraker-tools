"""Tests for the machine tools."""

from typing import Any, Dict, Generator
from unittest.mock import AsyncMock, patch

import pytest
from moonraker_tools.client import MoonrakerClient
from moonraker_tools.tools.machine import MachineTools


@pytest.fixture
def mock_client() -> Generator[AsyncMock, None, None]:
    """Fixture for a mocked MoonrakerClient."""
    with patch("moonraker_tools.client.MoonrakerClient", autospec=True) as mock:
        yield mock


@pytest.fixture
def machine_tools(mock_client: AsyncMock) -> MachineTools:
    """Fixture for MachineTools with a mocked client."""
    return MachineTools(mock_client)


@pytest.mark.asyncio
async def test_get_system_info(
    machine_tools: MachineTools, mock_client: AsyncMock
) -> None:
    """Test getting system info."""
    # Arrange
    mock_response: Dict[str, Any] = {
        "system_info": {
            "provider": "systemd_dbus",
            "cpu_info": {
                "cpu_count": 4,
                "bits": "32bit",
                "processor": "armv7l",
                "cpu_desc": "ARMv7 Processor rev 4 (v7l)",
                "serial_number": "b898bdb4",
                "hardware_desc": "BCM2835",
                "model": "Raspberry Pi 3 Model B Rev 1.2",
                "total_memory": 945364,
                "memory_units": "kB",
            },
        }
    }
    mock_client.get.return_value = mock_response

    # Act
    result = await machine_tools.get_system_info()

    # Assert
    mock_client.get.assert_called_once_with("/machine/system_info")
    assert result == mock_response
