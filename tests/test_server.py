"""Tests for the server tools."""

from typing import Any, Dict, Generator
from unittest.mock import AsyncMock, patch

import pytest
from moonraker_tools.client import MoonrakerClient
from moonraker_tools.tools.server import ServerTools


@pytest.fixture
def mock_client() -> Generator[AsyncMock, None, None]:
    """Fixture for a mocked MoonrakerClient."""
    with patch("moonraker_tools.client.MoonrakerClient", autospec=True) as mock:
        yield mock


@pytest.fixture
def server_tools(mock_client: AsyncMock) -> ServerTools:
    """Fixture for ServerTools with a mocked client."""
    return ServerTools(mock_client)


@pytest.mark.asyncio
async def test_get_info(server_tools: ServerTools, mock_client: AsyncMock) -> None:
    """Test getting server info."""
    # Arrange
    mock_response: Dict[str, Any] = {
        "klippy_connected": True,
        "klippy_state": "ready",
        "components": ["database", "file_manager"],
    }
    mock_client.get.return_value = mock_response

    # Act
    result = await server_tools.get_info()

    # Assert
    mock_client.get.assert_called_once_with("/server/info")
    assert result == mock_response
