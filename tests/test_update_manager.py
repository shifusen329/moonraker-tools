"""Tests for the update_manager tools."""

from typing import Any, Dict, Generator
from unittest.mock import AsyncMock, patch

import pytest
from moonraker_tools.client import MoonrakerClient
from moonraker_tools.tools.update_manager import UpdateManagerTools


@pytest.fixture
def mock_client() -> Generator[AsyncMock, None, None]:
    """Fixture for a mocked MoonrakerClient."""
    with patch("moonraker_tools.client.MoonrakerClient", autospec=True) as mock:
        yield mock


@pytest.fixture
def update_manager_tools(mock_client: AsyncMock) -> UpdateManagerTools:
    """Fixture for UpdateManagerTools with a mocked client."""
    return UpdateManagerTools(mock_client)


@pytest.mark.asyncio
async def test_get_status(
    update_manager_tools: UpdateManagerTools, mock_client: AsyncMock
) -> None:
    """Test getting the update status."""
    # Arrange
    mock_response: Dict[str, Any] = {
        "busy": False,
        "github_rate_limit": 60,
        "github_requests_remaining": 57,
        "github_limit_reset_time": 1615836932,
        "version_info": {},
    }
    mock_client.get.return_value = mock_response

    # Act
    result = await update_manager_tools.get_status()

    # Assert
    mock_client.get.assert_called_once_with("/machine/update/status")
    assert result == mock_response
