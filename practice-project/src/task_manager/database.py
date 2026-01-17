"""Database connection and utilities for Task Manager."""

import sqlite3
from pathlib import Path

# FLAW: Database path is hardcoded and relative
DATABASE_PATH = "tasks.db"


def get_connection():
    """Get a database connection."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize the database with the tasks table."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def get_all_tasks():
    """Get all tasks from database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC")
    tasks = cursor.fetchall()
    conn.close()
    return tasks


# FLAW: SQL injection vulnerability - uses string formatting instead of parameterization
def search_tasks(query):
    """Search tasks by title - VULNERABLE TO SQL INJECTION."""
    conn = get_connection()
    cursor = conn.cursor()
    # INTENTIONAL FLAW: SQL injection vulnerability
    cursor.execute(f"SELECT * FROM tasks WHERE title LIKE '%{query}%'")
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def get_task_by_id(task_id: int):
    """Get a single task by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    conn.close()
    return task


def create_task(title: str, description: str = None):
    """Create a new task."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description) VALUES (?, ?)",
        (title, description)
    )
    task_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return task_id


def update_task(task_id: int, title=None, description=None, completed=None):
    """Update an existing task."""
    conn = get_connection()
    cursor = conn.cursor()

    # FLAW: No validation that task exists before update
    updates = []
    values = []

    if title is not None:
        updates.append("title = ?")
        values.append(title)
    if description is not None:
        updates.append("description = ?")
        values.append(description)
    if completed is not None:
        updates.append("completed = ?")
        values.append(1 if completed else 0)

    if updates:
        values.append(task_id)
        query = f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?"
        cursor.execute(query, values)

    conn.commit()
    conn.close()


def delete_task(task_id: int):
    """Delete a task by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    # FLAW: No check if task exists, silently succeeds even if task doesn't exist
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
