from pydantic import BaseModel,EmailStr

class ContactCreate(BaseModel):
    name: str
    title: str
    email: EmailStr
    linkedin: str
    domain:str
