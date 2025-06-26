"""An MCP server for interacting with a Moonraker instance."""

import asyncio
import os

from dotenv import load_dotenv
from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
import mcp.server.stdio

from moonraker_tools.agent.file_manager import list_files
from moonraker_tools.agent.job_queue import get_job_queue_status
from moonraker_tools.agent.printer_operations import list_objects
from moonraker_tools.agent.printer_status import get_printer_status
from moonraker_tools.agent.webcam import download_snapshot

load_dotenv()

server = Server("moonraker-mcp")


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="get_printer_status",
            description="Get the current status of the printer.",
            inputSchema={"type": "object", "properties": {}},
        ),
        types.Tool(
            name="list_files",
            description="List available files in a root.",
            inputSchema={
                "type": "object",
                "properties": {"root": {"type": "string", "default": "gcodes"}},
            },
        ),
        types.Tool(
            name="get_job_queue_status",
            description="Get the current status of the job queue.",
            inputSchema={"type": "object", "properties": {}},
        ),
        types.Tool(
            name="list_objects",
            description="List loaded printer objects.",
            inputSchema={"type": "object", "properties": {}},
        ),
        types.Tool(
            name="download_snapshot",
            description="Download a snapshot from the webcam.",
            inputSchema={
                "type": "object",
                "properties": {
                    "webcam_name": {"type": "string"},
                    "output_path": {
                        "type": "string",
                        "default": "snapshot.jpg",
                    },
                },
            },
        ),
    ]


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle tool execution requests."""
    if arguments is None:
        arguments = {}

    if name == "get_printer_status":
        result = await get_printer_status()
    elif name == "list_files":
        result = await list_files(**arguments)
    elif name == "get_job_queue_status":
        result = await get_job_queue_status()
    elif name == "list_objects":
        result = await list_objects()
    elif name == "download_snapshot":
        result = await download_snapshot(**arguments)
    else:
        raise ValueError(f"Unknown tool: {name}")

    return [types.TextContent(type="text", text=str(result))]


async def main():
    """Run the MCP server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="moonraker-mcp",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(main())
