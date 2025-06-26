"""Tests for the announcements tools."""

from typing import Any, Dict, Generator, List
from unittest.mock import AsyncMock, patch

import pytest
from moonraker_tools.client import MoonrakerClient
from moonraker_tools.tools.announcements import AnnouncementsTools


@pytest.fixture
def mock_client() -> Generator[AsyncMock, None, None]:
    """Fixture for a mocked MoonrakerClient."""
    with patch("moonraker_tools.client.MoonrakerClient", autospec=True) as mock:
        yield mock


@pytest.fixture
def announcements_tools(mock_client: AsyncMock) -> AnnouncementsTools:
    """Fixture for AnnouncementsTools with a mocked client."""
    return AnnouncementsTools(mock_client)


@pytest.mark.asyncio
async def test_list_announcements(
    announcements_tools: AnnouncementsTools, mock_client: AsyncMock
) -> None:
    """Test listing announcements."""
    # Arrange
    mock_response: Dict[str, List[Dict[str, Any]]] = {
        "entries": [
            {
                "entry_id": "arksine/moonlight/issue/3",
                "url": "https://github.com/Arksine/moonlight/issues/3",
                "title": "Test announcement 3",
                "description": "Test Description",
                "priority": "normal",
                "date": 1647459219,
                "dismissed": False,
                "date_dismissed": None,
                "dismiss_wake": None,
                "source": "moonlight",
                "feed": "moonlight",
            }
        ],
        "feeds": ["moonraker", "klipper", "moonlight"],
    }
    mock_client.get.return_value = mock_response

    # Act
    result = await announcements_tools.list()

    # Assert
    mock_client.get.assert_called_once_with(
        "/server/announcements/list", params={"include_dismissed": False}
    )
    assert result == mock_response
