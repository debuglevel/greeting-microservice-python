import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
import app.rest
from app.rest import fastapi

client = TestClient(fastapi)

def test_get_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "up"}

def test_get_health_async():
    response = client.get("/health_async")
    assert response.status_code == 200
    assert response.json() == {"status": "up"}
