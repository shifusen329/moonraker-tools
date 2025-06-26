"""Tests for the webcams tools."""

from typing import Any, Dict, Generator, List
from unittest.mock import AsyncMock, patch

import pytest
from moonraker_tools.client import MoonrakerClient
from moonraker_tools.tools.webcams import WebcamsTools


@pytest.fixture
def mock_client() -> Generator[AsyncMock, None, None]:
    """Fixture for a mocked MoonrakerClient."""
    with patch("moonraker_tools.client.MoonrakerClient", autospec=True) as mock:
        yield mock


@pytest.fixture
def webcams_tools(mock_client: AsyncMock) -> WebcamsTools:
    """Fixture for WebcamsTools with a mocked client."""
    return WebcamsTools(mock_client)


@pytest.mark.asyncio
async def test_list_webcams(
    webcams_tools: WebcamsTools, mock_client: AsyncMock
) -> None:
    """Test listing webcams."""
    # Arrange
    mock_response: Dict[str, List[Dict[str, Any]]] = {
        "webcams": [
            {
                "name": "TestCam",
                "location": "printer",
                "service": "mjpegstreamer",
                "enabled": True,
                "icon": "mdiWebcam",
                "target_fps": 15,
                "target_fps_idle": 5,
                "stream_url": "/webcam/?action=stream",
                "snapshot_url": "/webcam/?action=snapshot",
                "flip_horizontal": False,
                "flip_vertical": False,
                "rotation": 0,
                "aspect_ratio": "4:3",
                "extra_data": {},
                "source": "database",
                "uid": "341778f9-387f-455b-8b69-ff68442d41d9",
            }
        ]
    }
    mock_client.get.return_value = mock_response

    # Act
    result = await webcams_tools.list_webcams()

    # Assert
    mock_client.get.assert_called_once_with("/server/webcams/list")
    assert result == mock_response
