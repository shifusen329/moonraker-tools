"""A script to take a snapshot from a Moonraker instance."""

import asyncio
from dotenv import load_dotenv
from moonraker_tools.agent.webcam import download_snapshot

load_dotenv()


async def main() -> None:
    """Take a snapshot."""
    print("Taking snapshot...")
    output_path = await download_snapshot(output_path="webcam_snapshot.jpg")
    print(f"Snapshot saved to: {output_path}")


if __name__ == "__main__":
    asyncio.run(main())
