"""Tests for the database tools."""

from typing import Any, Dict, Generator, List
from unittest.mock import AsyncMock, patch

import pytest
from moonraker_tools.client import MoonrakerClient
from moonraker_tools.tools.database import DatabaseTools


@pytest.fixture
def mock_client() -> Generator[AsyncMock, None, None]:
    """Fixture for a mocked MoonrakerClient."""
    with patch("moonraker_tools.client.MoonrakerClient", autospec=True) as mock:
        yield mock


@pytest.fixture
def database_tools(mock_client: AsyncMock) -> DatabaseTools:
    """Fixture for DatabaseTools with a mocked client."""
    return DatabaseTools(mock_client)


@pytest.mark.asyncio
async def test_list_namespaces(
    database_tools: DatabaseTools, mock_client: AsyncMock
) -> None:
    """Test listing namespaces."""
    # Arrange
    mock_response: Dict[str, List[str]] = {
        "namespaces": ["gcode_metadata", "webcams"]
    }
    mock_client.get.return_value = mock_response

    # Act
    result = await database_tools.list_namespaces()

    # Assert
    mock_client.get.assert_called_once_with("/server/database/list")
    assert result == mock_response
