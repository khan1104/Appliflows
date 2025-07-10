from fastapi import APIRouter,HTTPException,status
from schemas.auth import LoginData
from dotenv import load_dotenv
import os
load_dotenv()

router=APIRouter()

@router.post("/login",status_code=status.HTTP_200_OK)
def home(data:LoginData):
    if data.email==os.getenv("ADMIN_EMAIL") and data.password==os.getenv("ADMIN_PASSWORD"):
        return {"message":"sucessfull login"}
    else:
        raise HTTPException(detail="inavlid credentiasl",status_code=status.HTTP_401_UNAUTHORIZED)