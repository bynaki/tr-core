import asyncio

from tr_core import hello


def test_hello() -> None:
    assert hello() == "Hello from tr-core!"


async def test_async_runs() -> None:
    await asyncio.sleep(0)
