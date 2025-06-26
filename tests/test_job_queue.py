"""Tests for the job_queue tools."""

from typing import Any, Dict, Generator
from unittest.mock import AsyncMock, patch

import pytest
from moonraker_tools.client import MoonrakerClient
from moonraker_tools.tools.job_queue import JobQueueTools


@pytest.fixture
def mock_client() -> Generator[AsyncMock, None, None]:
    """Fixture for a mocked MoonrakerClient."""
    with patch("moonraker_tools.client.MoonrakerClient", autospec=True) as mock:
        yield mock


@pytest.fixture
def job_queue_tools(mock_client: AsyncMock) -> JobQueueTools:
    """Fixture for JobQueueTools with a mocked client."""
    return JobQueueTools(mock_client)


@pytest.mark.asyncio
async def test_get_status(
    job_queue_tools: JobQueueTools, mock_client: AsyncMock
) -> None:
    """Test getting the job queue status."""
    # Arrange
    mock_response: Dict[str, Any] = {
        "queued_jobs": [],
        "queue_state": "ready",
    }
    mock_client.get.return_value = mock_response

    # Act
    result = await job_queue_tools.get_status()

    # Assert
    mock_client.get.assert_called_once_with("/server/job_queue/status")
    assert result == mock_response
