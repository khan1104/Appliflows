from fastapi import APIRouter,HTTPException,status
from schemas.auth import LoginData

router=APIRouter()

@router.post("/login",status_code=status.HTTP_200_OK)
def home(data:LoginData):
    if data.email=="admin@gmail.com" and data.password=="admin":
        return {"message":"sucessfull login"}
    else:
        raise HTTPException(detail="inavlid credentiasl",status_code=status.HTTP_401_UNAUTHORIZED)