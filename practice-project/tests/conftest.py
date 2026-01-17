"""Pytest configuration and fixtures."""

import os
import pytest
from fastapi.testclient import TestClient

from task_manager import database
from task_manager.main import app


@pytest.fixture(scope="function")
def test_db(tmp_path):
    """Create a temporary test database."""
    db_path = tmp_path / "test_tasks.db"
    original_path = database.DATABASE_PATH
    database.DATABASE_PATH = str(db_path)
    database.init_db()
    yield db_path
    database.DATABASE_PATH = original_path


@pytest.fixture
def client(test_db):
    """Create a test client with clean database."""
    return TestClient(app)


@pytest.fixture
def sample_task(client):
    """Create a sample task for testing."""
    response = client.post("/tasks", json={
        "title": "Test Task",
        "description": "A test task description"
    })
    return response.json()
