from pydantic import BaseModel
from typing import Optional


class BugReport(BaseModel):
    title: str
    description: str
    stack_trace: Optional[str] = None
    error_log: Optional[str] = None
    severity: Optional[str] = "Medium"
