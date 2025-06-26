"""Tests for the extensions tools."""

from typing import Any, Dict, Generator, List
from unittest.mock import AsyncMock, patch

import pytest
from moonraker_tools.client import MoonrakerClient
from moonraker_tools.tools.extensions import ExtensionsTools


@pytest.fixture
def mock_client() -> Generator[AsyncMock, None, None]:
    """Fixture for a mocked MoonrakerClient."""
    with patch("moonraker_tools.client.MoonrakerClient", autospec=True) as mock:
        yield mock


@pytest.fixture
def extensions_tools(mock_client: AsyncMock) -> ExtensionsTools:
    """Fixture for ExtensionsTools with a mocked client."""
    return ExtensionsTools(mock_client)


@pytest.mark.asyncio
async def test_list_extensions(
    extensions_tools: ExtensionsTools, mock_client: AsyncMock
) -> None:
    """Test listing extensions."""
    # Arrange
    mock_response: Dict[str, List[Dict[str, Any]]] = {
        "agents": [
            {
                "name": "moonagent",
                "version": "0.0.1",
                "type": "agent",
                "url": "https://github.com/arksine/moontest",
            }
        ]
    }
    mock_client.get.return_value = mock_response

    # Act
    result = await extensions_tools.list_extensions()

    # Assert
    mock_client.get.assert_called_once_with("/server/extensions/list")
    assert result == mock_response
