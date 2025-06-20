from pydantic import BaseModel
from typing import Optional

class IdiomRequest(BaseModel):
    nbr_idioms: int
    topic: str
    level: str
    session_id: Optional[str] = "default"

class SessionInput(BaseModel):
    session_id: Optional[str] = "default"

class UserAnswerInput(BaseModel):
    user_answer: str
    session_id: str = "default"