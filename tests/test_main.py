import pytest
import app.main

#@pytest.mark.asyncio
#async def test_health():
def test_health():
    status = app.main.get_health()["status"]
    assert status == "up"
