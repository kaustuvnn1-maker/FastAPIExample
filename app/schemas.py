from datetime import time
from typing import Optional
from unittest.mock import Base
from pydantic import BaseModel,EmailStr
class PostBase(BaseModel):
    title:str
    content:str
    published:bool = True

class CreatePost(PostBase):
    pass

class UpdatePost(PostBase):
    pass
class CreateUser(BaseModel):
    emailid:EmailStr
    password:str
class userIDResponse(BaseModel):
    emailid:EmailStr
    createdTime:time
class userLogin(BaseModel):
    email:EmailStr
    password: str
class Token(BaseModel):
    accessToken : str
    token_type : str
class TokenData(BaseModel):
    id: Optional[str]