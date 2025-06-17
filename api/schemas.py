from pydantic import BaseModel
from typing import Optional

class IdiomRequest(BaseModel):
    nbr_idioms: int
    topic: str
    level: str
    session_id: Optional[str] = "default"

# class MatchingExerciseRequest(BaseModel):
#     idioms: str
#     do_training: str

# class EvalRequest(BaseModel):
#     user_sentence: str
#     idiom: str

# class MatchingExerciseResponse(BaseModel):
#     german_idioms: list[str]
#     english_meanings: list[str]
