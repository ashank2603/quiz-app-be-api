from fastapi import FastAPI
from routes import quiz, user

app = FastAPI(
    title="Fibr Quiz Task Backend"
)

app.include_router(user.router)
app.include_router(quiz.router)