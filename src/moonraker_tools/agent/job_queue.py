"""Agent tools for interacting with the Moonraker job_queue API."""

import os
from typing import Any, Dict, List

from ..client import MoonrakerClient
from ..tools.job_queue import JobQueueTools


async def get_job_queue_status() -> Dict[str, Any]:
    """
    Get the current status of the job queue.

    Returns:
        A dictionary containing the job queue status.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    job_queue_tools = JobQueueTools(client)

    try:
        status = await job_queue_tools.get_status()
    finally:
        await client.close()

    return status


async def enqueue_job(filenames: List[str], reset: bool = False) -> Dict[str, Any]:
    """
    Enqueue one or more jobs.

    Args:
        filenames: A list of filenames to enqueue.
        reset: Whether to clear the queue before adding the new jobs.

    Returns:
        A dictionary containing the updated job queue status.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    job_queue_tools = JobQueueTools(client)

    try:
        result = await job_queue_tools.enqueue_job(filenames=filenames, reset=reset)
    finally:
        await client.close()

    return result


async def remove_job(
    job_ids: List[str] = None, all_jobs: bool = False
) -> Dict[str, Any]:
    """
    Remove one or more jobs from the queue.

    Args:
        job_ids: A list of job IDs to remove.
        all_jobs: If True, all jobs will be removed from the queue.

    Returns:
        A dictionary containing the updated job queue status.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    job_queue_tools = JobQueueTools(client)

    try:
        result = await job_queue_tools.remove_job(job_ids=job_ids, all_jobs=all_jobs)
    finally:
        await client.close()

    return result


async def pause_queue() -> Dict[str, Any]:
    """
    Pause the job queue.

    Returns:
        A dictionary containing the updated job queue status.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    job_queue_tools = JobQueueTools(client)

    try:
        result = await job_queue_tools.pause_queue()
    finally:
        await client.close()

    return result


async def start_queue() -> Dict[str, Any]:
    """
    Start the job queue.

    Returns:
        A dictionary containing the updated job queue status.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    job_queue_tools = JobQueueTools(client)

    try:
        result = await job_queue_tools.start_queue()
    finally:
        await client.close()

    return result


async def jump_to_job(job_id: str) -> Dict[str, Any]:
    """
    Jump a job to the front of the queue.

    Args:
        job_id: The ID of the job to jump.

    Returns:
        A dictionary containing the updated job queue status.
    """
    host = os.getenv("MOONRAKER_HOST")
    port = os.getenv("MOONRAKER_PORT")
    api_key = os.getenv("MOONRAKER_API_KEY")

    if not host or not port:
        raise ValueError(
            "MOONRAKER_HOST and MOONRAKER_PORT must be set in the .env file."
        )

    client = MoonrakerClient(host=host, port=int(port), api_key=api_key)
    job_queue_tools = JobQueueTools(client)

    try:
        result = await job_queue_tools.jump_to_job(job_id=job_id)
    finally:
        await client.close()

    return result
