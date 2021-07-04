import pytest
import app.health

def test_health():
    status = app.health.get_health()["status"]
    assert status == "up"

@pytest.mark.asyncio
async def test_health_async():
    status = (await app.health.get_health_async())["status"]
    assert status == "up"

