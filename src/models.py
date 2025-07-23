from pydantic import BaseModel
from typing import List, Optional


class SupportTicket(BaseModel):
    subject: str
    description: str


class SupportState(BaseModel):
    ticket: SupportTicket
    category: Optional[str] = None
    context: List[str] = []
    draft: Optional[str] = None
    reviewer_feedback: Optional[str] = None
    attempts: int = 0
