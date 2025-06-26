"""Tests for the file_manager tools."""

from typing import Any, Dict, Generator, List
from unittest.mock import AsyncMock, patch

import pytest
from moonraker_tools.client import MoonrakerClient
from moonraker_tools.tools.file_manager import FileManagerTools


@pytest.fixture
def mock_client() -> Generator[AsyncMock, None, None]:
    """Fixture for a mocked MoonrakerClient."""
    with patch("moonraker_tools.client.MoonrakerClient", autospec=True) as mock:
        yield mock


@pytest.fixture
def file_manager_tools(mock_client: AsyncMock) -> FileManagerTools:
    """Fixture for FileManagerTools with a mocked client."""
    return FileManagerTools(mock_client)


@pytest.mark.asyncio
async def test_list_files(
    file_manager_tools: FileManagerTools, mock_client: AsyncMock
) -> None:
    """Test listing files."""
    # Arrange
    mock_response: List[Dict[str, Any]] = [
        {
            "path": "test.gcode",
            "modified": 1615077020.2025201,
            "size": 4926481,
            "permissions": "rw",
        }
    ]
    mock_client.get.return_value = mock_response

    # Act
    result = await file_manager_tools.list_files()

    # Assert
    mock_client.get.assert_called_once_with(
        "/server/files/list", params={"root": "gcodes"}
    )
    assert result == mock_response
