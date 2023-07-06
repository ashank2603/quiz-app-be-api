import os
from jose import jwt
from jose.jwt import ExpiredSignatureError, JWTError
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

def generate_jwt_token(email: str, userId: str):
    expdelta = timedelta(weeks=1)
    now = datetime.utcnow()
    exp = now + expdelta
    payload = {
        'nbf': now,
        'iat': now,
        'exp': exp,
        'sub': email,
        'userId': userId
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
    return token

def verify_jwt_token(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET_KEY)
        return decoded_token
    except ExpiredSignatureError:
        return {"message": "Token expired!"}
    except JWTError:
        return {"message": "Error validating token"}