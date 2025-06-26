"""Tests for the printer tools."""

from typing import Any, Dict, Generator
from unittest.mock import AsyncMock, patch

import pytest
from moonraker_tools.client import MoonrakerClient
from moonraker_tools.tools.printer import PrinterTools


@pytest.fixture
def mock_client() -> Generator[AsyncMock, None, None]:
    """Fixture for a mocked MoonrakerClient."""
    with patch("moonraker_tools.client.MoonrakerClient", autospec=True) as mock:
        yield mock


@pytest.fixture
def printer_tools(mock_client: AsyncMock) -> PrinterTools:
    """Fixture for PrinterTools with a mocked client."""
    return PrinterTools(mock_client)


@pytest.mark.asyncio
async def test_get_info(printer_tools: PrinterTools, mock_client: AsyncMock) -> None:
    """Test getting printer info."""
    # Arrange
    mock_response: Dict[str, Any] = {
        "state": "ready",
        "state_message": "Printer is ready",
        "hostname": "pi-debugger",
    }
    mock_client.get.return_value = mock_response

    # Act
    result = await printer_tools.get_info()

    # Assert
    mock_client.get.assert_called_once_with("/printer/info")
    assert result == mock_response
