from pydantic import BaseModel

class CreateUser(BaseModel):
    name: str = ""
    email: str = ""
    password: str = ""

class LoginUser(BaseModel):
    email: str = ""
    password: str = ""