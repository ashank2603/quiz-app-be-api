from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from models.user import CreateUser, LoginUser
from passlib.context import CryptContext
from prisma import Prisma
from prisma.errors import UniqueViolationError, RecordNotFoundError
from utils.jwt_util import generate_jwt_token

router = APIRouter(prefix="/user", tags=["User"])
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return bcrypt_context.hash(password)

def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)

@router.post("/login")
async def login(user: LoginUser):
    try:
        prisma = Prisma()
        await prisma.connect()
        existing_user = await prisma.user.find_first_or_raise(
            where={
                "email": user.email
            }
        )
        if verify_password(user.password, existing_user.hashedPassword):
            return JSONResponse({"accessToken": generate_jwt_token(existing_user.email, existing_user.id)})
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials!")
    except RecordNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found!")
    finally:
        await prisma.disconnect()

@router.post("/signup")
async def signup(user: CreateUser):
    try:
        prisma = Prisma()
        await prisma.connect()

        new_user = await prisma.user.create(
            data={
                "name": user.name,
                "email": user.email,
                "hashedPassword": get_password_hash(user.password)
            }
        )
        return JSONResponse({"message": "User Created Successfully!"}, status_code=status.HTTP_201_CREATED)
    except UniqueViolationError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with email already exists!")
    finally:
        await prisma.disconnect()