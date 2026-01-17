"""API routes for Task Manager."""

from fastapi import APIRouter, HTTPException

from . import database
from .models import Task, TaskCreate, TaskUpdate

router = APIRouter()


@router.get("/tasks")
def list_tasks():
    """List all tasks."""
    tasks = database.get_all_tasks()
    # FLAW: Manual conversion instead of using Pydantic properly
    result = []
    for task in tasks:
        result.append({
            "id": task["id"],
            "title": task["title"],
            "description": task["description"],
            "completed": bool(task["completed"]),
            "created_at": task["created_at"]
        })
    return result


@router.get("/tasks/search")
def search_tasks(q: str):
    """Search tasks by title - WARNING: SQL injection vulnerable."""
    # FLAW: No input validation on search query
    tasks = database.search_tasks(q)
    result = []
    for task in tasks:
        result.append({
            "id": task["id"],
            "title": task["title"],
            "description": task["description"],
            "completed": bool(task["completed"]),
            "created_at": task["created_at"]
        })
    return result


@router.post("/tasks")
def create_task(task: TaskCreate):
    """Create a new task."""
    # FLAW: No validation of title length or content
    task_id = database.create_task(task.title, task.description)

    # FLAW: Duplicated code - same conversion as above
    new_task = database.get_task_by_id(task_id)
    return {
        "id": new_task["id"],
        "title": new_task["title"],
        "description": new_task["description"],
        "completed": bool(new_task["completed"]),
        "created_at": new_task["created_at"]
    }


@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    """Get a task by ID."""
    task = database.get_task_by_id(task_id)

    # FLAW: Inconsistent error handling - raises generic exception
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    # FLAW: Duplicated conversion code again
    return {
        "id": task["id"],
        "title": task["title"],
        "description": task["description"],
        "completed": bool(task["completed"]),
        "created_at": task["created_at"]
    }


@router.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    """Update a task."""
    # FLAW: No check if task exists before update
    existing = database.get_task_by_id(task_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Task not found")

    database.update_task(
        task_id,
        title=task_update.title,
        description=task_update.description,
        completed=task_update.completed
    )

    # FLAW: Yet more duplicated conversion code
    updated_task = database.get_task_by_id(task_id)
    return {
        "id": updated_task["id"],
        "title": updated_task["title"],
        "description": updated_task["description"],
        "completed": bool(updated_task["completed"]),
        "created_at": updated_task["created_at"]
    }


# FLAW: Inconsistent naming - uses 'deleteTask' style comment but 'delete_task' function
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """Delete a task."""
    # FLAW: No check if task exists, just deletes silently
    existing = database.get_task_by_id(task_id)
    if not existing:
        raise HTTPException(status_code=404, detail="not found")  # FLAW: Inconsistent error message

    database.delete_task(task_id)
    return {"message": "Task deleted"}  # FLAW: Inconsistent response format


# FLAW: Missing type hints on this function
def convert_task_row(row):
    """Convert a database row to a dict - helper that should be used but isn't."""
    return {
        "id": row["id"],
        "title": row["title"],
        "description": row["description"],
        "completed": bool(row["completed"]),
        "created_at": row["created_at"]
    }
