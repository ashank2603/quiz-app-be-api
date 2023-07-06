from pydantic import BaseModel
from typing import Optional, List

class CreateQuiz(BaseModel):
    quizTitle: str = ""
    quizDescription: Optional[str] = ""

class CreateQuestion(BaseModel):
    question: str = ""
    options: List[str] = []
    correctOptions: List[str] = []
    pointsAwarded: int = 1