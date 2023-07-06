from pydantic import BaseModel

class CreateUser(BaseModel):
    name: str = ""
    email: str = ""
    password: str = ""

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "name": "<YOUR_NAME>",
    #             "email": "<YOUR_EMAIL>",
    #             "password": "<YOUR_PASSWORD>"
    #         }
    #     }

class LoginUser(BaseModel):
    email: str = ""
    password: str = ""