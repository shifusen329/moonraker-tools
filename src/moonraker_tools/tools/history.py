"""Tools for interacting with the Moonraker history API."""

from typing import Any, Dict, List, Optional

from ..client import MoonrakerClient


class HistoryTools:
    """A class to encapsulate history-related API endpoints."""

    def __init__(self, client: MoonrakerClient) -> None:
        """
        Initialize the HistoryTools with a MoonrakerClient instance.

        Args:
            client: An instance of MoonrakerClient.
        """
        self._client = client

    async def list_jobs(
        self,
        limit: Optional[int] = None,
        start: Optional[int] = None,
        since: Optional[float] = None,
        before: Optional[float] = None,
        order: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Get the list of historical jobs.

        Args:
            limit: The maximum number of jobs to return.
            start: The starting record number.
            since: A timestamp to limit jobs to after this date.
            before: A timestamp to limit jobs to before this date.
            order: The order of the returned list (asc or desc).

        Returns:
            A dictionary containing the list of jobs and the total count.
        """
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if start is not None:
            params["start"] = start
        if since is not None:
            params["since"] = since
        if before is not None:
            params["before"] = before
        if order is not None:
            params["order"] = order
        return await self._client.get("/server/history/list", params=params)

    async def get_totals(self) -> Dict[str, Any]:
        """
        Get the job totals.

        Returns:
            A dictionary containing job totals.
        """
        return await self._client.get("/server/history/totals")

    async def reset_totals(self) -> Dict[str, Any]:
        """
        Reset the job totals.

        Returns:
            A dictionary containing the last totals before the reset.
        """
        return await self._client.post("/server/history/reset_totals")

    async def get_job(self, uid: str) -> Dict[str, Any]:
        """
        Get a single job by its UID.

        Args:
            uid: The unique identifier for the job.

        Returns:
            A dictionary containing the job details.
        """
        params = {"uid": uid}
        return await self._client.get("/server/history/job", params=params)

    async def delete_job(
        self, uid: Optional[str] = None, all_jobs: bool = False
    ) -> Dict[str, List[str]]:
        """
        Delete one or all jobs.

        Args:
            uid: The unique identifier for the job to delete.
            all_jobs: If True, all jobs will be deleted.

        Returns:
            A dictionary containing a list of the deleted job UIDs.
        """
        params: Dict[str, Any] = {}
        if all_jobs:
            params["all"] = True
        elif uid:
            params["uid"] = uid
        else:
            raise ValueError("Either uid or all_jobs must be specified.")
        return await self._client.delete("/server/history/job", params=params)
