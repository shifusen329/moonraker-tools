"""Tools for interacting with the Moonraker job_queue API."""

from typing import Any, Dict, List

from ..client import MoonrakerClient


class JobQueueTools:
    """A class to encapsulate job_queue-related API endpoints."""

    def __init__(self, client: MoonrakerClient) -> None:
        """
        Initialize the JobQueueTools with a MoonrakerClient instance.

        Args:
            client: An instance of MoonrakerClient.
        """
        self._client = client

    async def get_status(self) -> Dict[str, Any]:
        """
        Get the current status of the job queue.

        Returns:
            A dictionary containing the job queue status.
        """
        return await self._client.get("/server/job_queue/status")

    async def enqueue_job(
        self, filenames: List[str], reset: bool = False
    ) -> Dict[str, Any]:
        """
        Enqueue one or more jobs.

        Args:
            filenames: A list of filenames to enqueue.
            reset: Whether to clear the queue before adding the new jobs.

        Returns:
            A dictionary containing the updated job queue status.
        """
        data = {"filenames": filenames, "reset": reset}
        return await self._client.post("/server/job_queue/job", data=data)

    async def remove_job(
        self, job_ids: List[str] = None, all_jobs: bool = False
    ) -> Dict[str, Any]:
        """
        Remove one or more jobs from the queue.

        Args:
            job_ids: A list of job IDs to remove.
            all_jobs: If True, all jobs will be removed from the queue.

        Returns:
            A dictionary containing the updated job queue status.
        """
        params: Dict[str, Any] = {}
        if all_jobs:
            params["all"] = True
        elif job_ids:
            params["job_ids"] = job_ids
        else:
            raise ValueError("Either job_ids or all_jobs must be specified.")
        return await self._client.delete("/server/job_queue/job", params=params)

    async def pause_queue(self) -> Dict[str, Any]:
        """
        Pause the job queue.

        Returns:
            A dictionary containing the updated job queue status.
        """
        return await self._client.post("/server/job_queue/pause")

    async def start_queue(self) -> Dict[str, Any]:
        """
        Start the job queue.

        Returns:
            A dictionary containing the updated job queue status.
        """
        return await self._client.post("/server/job_queue/start")

    async def jump_to_job(self, job_id: str) -> Dict[str, Any]:
        """
        Jump a job to the front of the queue.

        Args:
            job_id: The ID of the job to jump.

        Returns:
            A dictionary containing the updated job queue status.
        """
        params = {"job_id": job_id}
        return await self._client.post("/server/job_queue/jump", params=params)
