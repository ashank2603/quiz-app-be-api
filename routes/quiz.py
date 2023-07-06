from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from models.quiz import CreateQuiz
from prisma import Prisma
from prisma.errors import PrismaError
from utils.jwt_util import verify_jwt_token

router = APIRouter(prefix="/quiz", tags=["Quiz"])
auth_token_scheme = HTTPBearer()

@router.get("/")
def get_all_quizzes():
    pass

@router.get("/{quizId}")
def get_quiz_by_id():
    pass

@router.post("/create")
async def create_quiz(quiz: CreateQuiz, token: str = Depends(auth_token_scheme)):
    token_check = verify_jwt_token(token.credentials)
    if token_check["status"] == 200:
        user_info = token_check["decodedToken"]
        try:
            prisma = Prisma()
            await prisma.connect()
            new_quiz = await prisma.quiz.create(
                data={
                    "quizTitle": quiz.quizTitle,
                    "quizDescription": quiz.quizDescription,
                    "ownerId": user_info["userId"]
                }
            )
            return JSONResponse({"message": "Quiz Created Successfully!"}, status_code=status.HTTP_201_CREATED)
        except PrismaError as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Something Went Wrong!")
        finally:
            await prisma.disconnect()
    else:
        raise HTTPException(status_code=token_check["status"], detail=token_check["error"])

@router.post("/{quizId}/add")
def add_questions_to_quiz():
    pass