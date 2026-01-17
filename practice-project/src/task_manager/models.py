"""Pydantic models for Task Manager API."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TaskCreate(BaseModel):
    """Model for creating a new task."""

    title: str
    description: Optional[str] = None


class TaskUpdate(BaseModel):
    """Model for updating a task."""

    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class Task(BaseModel):
    """Model for task response."""

    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: str

    class Config:
        from_attributes = True
