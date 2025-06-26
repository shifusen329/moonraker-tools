"""Tests for the authorization tools."""

from typing import Any, Dict, Generator
from unittest.mock import AsyncMock, patch

import pytest
from moonraker_tools.client import MoonrakerClient
from moonraker_tools.tools.authorization import AuthorizationTools


@pytest.fixture
def mock_client() -> Generator[AsyncMock, None, None]:
    """Fixture for a mocked MoonrakerClient."""
    with patch("moonraker_tools.client.MoonrakerClient", autospec=True) as mock:
        yield mock


@pytest.fixture
def authorization_tools(mock_client: AsyncMock) -> AuthorizationTools:
    """Fixture for AuthorizationTools with a mocked client."""
    return AuthorizationTools(mock_client)


@pytest.mark.asyncio
async def test_login(
    authorization_tools: AuthorizationTools, mock_client: AsyncMock
) -> None:
    """Test logging in a user."""
    # Arrange
    mock_response: Dict[str, Any] = {
        "username": "testuser",
        "token": "some_jwt_token",
        "refresh_token": "some_refresh_token",
        "action": "user_logged_in",
        "source": "moonraker",
    }
    mock_client.post.return_value = mock_response

    # Act
    result = await authorization_tools.login("testuser", "password")

    # Assert
    mock_client.post.assert_called_once_with(
        "/access/login",
        data={"username": "testuser", "password": "password"},
    )
    assert result == mock_response
