from pydantic import BaseModel,EmailStr,AnyHttpUrl
from datetime import datetime


class CreateCompany(BaseModel):
    name:str
    website:AnyHttpUrl
    funding_stage: str

class ResponseData(BaseModel):
    id:int
    name:str
    website:str
    funding_stage:str
    created_at:datetime


