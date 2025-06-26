"""Integration tests for the Moonraker client."""

import os

import pytest
from dotenv import load_dotenv
from moonraker_tools.agent.file_manager import list_files
from moonraker_tools.agent.job_queue import get_job_queue_status
from moonraker_tools.agent.printer_operations import list_objects
from moonraker_tools.agent.printer_status import get_printer_status
from moonraker_tools.agent.webcam import download_snapshot

load_dotenv()


@pytest.mark.asyncio
async def test_get_printer_status() -> None:
    """Test getting the printer status."""
    # Act
    response = await get_printer_status()

    # Assert
    assert response is not None
    assert "result" in response
    assert "state" in response["result"]


@pytest.mark.asyncio
async def test_list_files() -> None:
    """Test listing files."""
    # Act
    response = await list_files()

    # Assert
    assert response is not None
    assert "result" in response


@pytest.mark.asyncio
async def test_get_job_queue_status() -> None:
    """Test getting the job queue status."""
    # Act
    response = await get_job_queue_status()

    # Assert
    assert response is not None
    assert "result" in response
    assert "queue_state" in response["result"]


@pytest.mark.asyncio
async def test_list_objects() -> None:
    """Test listing printer objects."""
    # Act
    response = await list_objects()

    # Assert
    assert response is not None
    assert "result" in response
    assert "objects" in response["result"]


@pytest.mark.asyncio
async def test_download_snapshot() -> None:
    """Test downloading a snapshot."""
    # Act
    output_path = await download_snapshot()

    # Assert
    assert os.path.exists(output_path)
    os.remove(output_path)
