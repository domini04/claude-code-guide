"""Tests for Task Manager API - INTENTIONALLY INCOMPLETE."""

import pytest
from fastapi.testclient import TestClient


class TestRoot:
    """Tests for root endpoints."""

    def test_root_endpoint(self, client):
        """Test the root endpoint returns API info."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data

    def test_health_check(self, client):
        """Test health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"


class TestTaskCreate:
    """Tests for task creation."""

    def test_create_task_success(self, client):
        """Test creating a task with valid data."""
        response = client.post("/tasks", json={
            "title": "New Task",
            "description": "Task description"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "New Task"
        assert data["description"] == "Task description"
        assert data["completed"] is False
        assert "id" in data
        assert "created_at" in data

    def test_create_task_without_description(self, client):
        """Test creating a task without description."""
        response = client.post("/tasks", json={
            "title": "Task Without Description"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Task Without Description"
        assert data["description"] is None

    # MISSING: Test for empty title
    # MISSING: Test for very long title
    # MISSING: Test for special characters in title


class TestTaskRead:
    """Tests for reading tasks."""

    def test_list_tasks_empty(self, client):
        """Test listing tasks when database is empty."""
        response = client.get("/tasks")
        assert response.status_code == 200
        assert response.json() == []

    def test_list_tasks_with_data(self, client, sample_task):
        """Test listing tasks returns created tasks."""
        response = client.get("/tasks")
        assert response.status_code == 200
        tasks = response.json()
        assert len(tasks) >= 1

    def test_get_task_by_id(self, client, sample_task):
        """Test getting a specific task by ID."""
        task_id = sample_task["id"]
        response = client.get(f"/tasks/{task_id}")
        assert response.status_code == 200
        assert response.json()["id"] == task_id

    def test_get_nonexistent_task(self, client):
        """Test getting a task that doesn't exist."""
        response = client.get("/tasks/99999")
        assert response.status_code == 404

    # MISSING: Test for invalid task_id type (string instead of int)


class TestTaskUpdate:
    """Tests for updating tasks."""

    def test_update_task_title(self, client, sample_task):
        """Test updating task title."""
        task_id = sample_task["id"]
        response = client.put(f"/tasks/{task_id}", json={
            "title": "Updated Title"
        })
        assert response.status_code == 200
        assert response.json()["title"] == "Updated Title"

    # MISSING: Test for updating completion status
    # MISSING: Test for updating description
    # MISSING: Test for updating nonexistent task
    # MISSING: Test for partial updates


class TestTaskDelete:
    """Tests for deleting tasks."""

    def test_delete_task(self, client, sample_task):
        """Test deleting an existing task."""
        task_id = sample_task["id"]
        response = client.delete(f"/tasks/{task_id}")
        assert response.status_code == 200

        # Verify task is deleted
        get_response = client.get(f"/tasks/{task_id}")
        assert get_response.status_code == 404

    # MISSING: Test for deleting nonexistent task


class TestTaskSearch:
    """Tests for search functionality."""

    # MISSING: All search tests
    # MISSING: SQL injection tests (security)
    pass


# MISSING: Integration tests
# MISSING: Edge case tests
# MISSING: Error handling tests
