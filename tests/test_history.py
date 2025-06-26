"""Tests for the history tools."""

from typing import Any, Dict, Generator, List
from unittest.mock import AsyncMock, patch

import pytest
from moonraker_tools.client import MoonrakerClient
from moonraker_tools.tools.history import HistoryTools


@pytest.fixture
def mock_client() -> Generator[AsyncMock, None, None]:
    """Fixture for a mocked MoonrakerClient."""
    with patch("moonraker_tools.client.MoonrakerClient", autospec=True) as mock:
        yield mock


@pytest.fixture
def history_tools(mock_client: AsyncMock) -> HistoryTools:
    """Fixture for HistoryTools with a mocked client."""
    return HistoryTools(mock_client)


@pytest.mark.asyncio
async def test_list_jobs(history_tools: HistoryTools, mock_client: AsyncMock) -> None:
    """Test listing jobs."""
    # Arrange
    mock_response: Dict[str, Any] = {
        "count": 1,
        "jobs": [
            {
                "job_id": "000001",
                "exists": True,
                "end_time": 1615764265.6493807,
                "filament_used": 7.83,
                "filename": "test/history_test.gcode",
                "metadata": {},
                "print_duration": 18.37201827496756,
                "status": "completed",
                "start_time": 1615764496.622146,
                "total_duration": 18.37201827496756,
                "user": "testuser",
                "auxiliary_data": [],
            }
        ],
    }
    mock_client.get.return_value = mock_response

    # Act
    result = await history_tools.list_jobs()

    # Assert
    mock_client.get.assert_called_once_with("/server/history/list", params={})
    assert result == mock_response
