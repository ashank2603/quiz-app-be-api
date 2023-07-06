from fastapi import APIRouter

router = APIRouter(prefix="/quiz", tags=["Quiz"])

@router.get("/")
def get_all_quizzes():
    pass

@router.get("/{quizId}")
def get_quiz_by_id():
    pass

@router.post("/create")
def create_quiz():
    pass

@router.post("/{quizId}/add")
def add_questions_to_quiz():
    pass