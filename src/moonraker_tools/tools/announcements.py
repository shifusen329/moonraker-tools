"""Tools for interacting with the Moonraker announcements API."""

from typing import Any, Dict, List, Optional

from ..client import MoonrakerClient


class AnnouncementsTools:
    """A class to encapsulate announcements-related API endpoints."""

    def __init__(self, client: MoonrakerClient) -> None:
        """
        Initialize the AnnouncementsTools with a MoonrakerClient instance.

        Args:
            client: An instance of MoonrakerClient.
        """
        self._client = client

    async def list(self, include_dismissed: bool = False) -> Dict[str, Any]:
        """
        Retrieve a list of current announcements.

        Args:
            include_dismissed: If True, dismissed announcements will be included.

        Returns:
            A dictionary containing the list of announcements and feeds.
        """
        params = {"include_dismissed": include_dismissed}
        return await self._client.get("/server/announcements/list", params=params)

    async def update(self) -> Dict[str, Any]:
        """
        Request that Moonraker check for announcement updates.

        Returns:
            A dictionary containing the list of announcements and a modified flag.
        """
        return await self._client.post("/server/announcements/update")

    async def dismiss(
        self, entry_id: str, wake_time: Optional[float] = None
    ) -> Dict[str, str]:
        """
        Dismiss an announcement.

        Args:
            entry_id: The ID of the announcement to dismiss.
            wake_time: A time in seconds after which the announcement will re-appear.

        Returns:
            A dictionary containing the entry_id of the dismissed announcement.
        """
        data = {"entry_id": entry_id}
        if wake_time is not None:
            data["wake_time"] = wake_time
        return await self._client.post("/server/announcements/dismiss", data=data)

    async def list_feeds(self) -> Dict[str, List[str]]:
        """
        List all announcement feeds.

        Returns:
            A dictionary containing a list of announcement feeds.
        """
        return await self._client.get("/server/announcements/feeds")

    async def subscribe_feed(self, name: str) -> Dict[str, str]:
        """
        Subscribe to an announcement feed.

        Args:
            name: The name of the feed to subscribe to.

        Returns:
            A dictionary containing the feed name and the action taken.
        """
        return await self._client.post(
            "/server/announcements/feed", data={"name": name}
        )

    async def remove_feed(self, name: str) -> Dict[str, str]:
        """
        Remove a subscribed announcement feed.

        Args:
            name: The name of the feed to remove.

        Returns:
            A dictionary containing the feed name and the action taken.
        """
        params = {"name": name}
        return await self._client.delete("/server/announcements/feed", params=params)
