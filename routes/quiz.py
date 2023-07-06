from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from models.quiz import CreateQuiz, CreateQuestion
from prisma import Prisma
from prisma.errors import PrismaError, RecordNotFoundError
from utils.jwt_util import verify_jwt_token

router = APIRouter(prefix="/quiz", tags=["Quiz"])
auth_token_scheme = HTTPBearer()

@router.get("/")
def get_all_quizzes():
    pass

@router.get("/{quizId}")
async def get_quiz_by_id(quizId, token: str = Depends(auth_token_scheme)):
    token_check = verify_jwt_token(token.credentials)
    if token_check["status"] == 200:
        user_info = token_check["decodedToken"]
        try:
            prisma = Prisma()
            await prisma.connect()
            quiz = await prisma.quiz.find_first_or_raise(
                where={
                    "id": quizId
                },
                include={
                    "questions": True
                }
            )
            return quiz
        except RecordNotFoundError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found!")
        finally:
            await prisma.disconnect()
    else:
        raise HTTPException(status_code=token_check["status"], detail=token_check["error"])

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
async def add_questions_to_quiz(question: CreateQuestion, quizId: str, token: str = Depends(auth_token_scheme)):
    token_check = verify_jwt_token(token.credentials)
    user_info = token_check["decodedToken"]
    if token_check["status"] == 200:
        user_info = token_check["decodedToken"]
        try:
            prisma = Prisma()
            await prisma.connect()
            existing_quiz = await prisma.quiz.find_first_or_raise(
                where={
                    "id": quizId
                }
            )
            if existing_quiz.ownerId == user_info["userId"]:
                new_question = await prisma.question.create(
                    data={
                        "question": question.question,
                        "options": question.options,
                        "correctOptions": question.correctOptions,
                        "pointsAwarded": question.pointsAwarded,
                        "quizId": quizId
                    }
                )
                return JSONResponse({"message": "Question Added!"}, status_code=status.HTTP_201_CREATED)
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorized for this action")
        except PrismaError as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Something Went Wrong!")
        finally:
            await prisma.disconnect()
    else:
        raise HTTPException(status_code=token_check["status"], detail=token_check["error"])