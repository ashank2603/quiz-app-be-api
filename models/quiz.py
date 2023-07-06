from pydantic import BaseModel
from typing import Optional

class CreateQuiz(BaseModel):
    quizTitle: str = ""
    quizDescription: Optional[str] = ""