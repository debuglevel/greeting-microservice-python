import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
import app.main
from app.main import fastapi

#@pytest.mark.asyncio
#async def test_health():
def test_health():
    status = app.main.get_health()["status"]
    assert status == "up"

client = TestClient(fastapi)

def test_get_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "up"}
