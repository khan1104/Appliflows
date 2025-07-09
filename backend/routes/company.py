from fastapi import APIRouter,HTTPException,status,Depends
from schemas.company import CreateCompany,ResponseData
from models.company import Company
from sqlalchemy.orm import Session
from config.databse import get_db
from datetime import datetime
from urllib.parse import urlparse

router=APIRouter()

def extract_domain(url_or_domain: str) -> str:
    """
    this function removes protocols and www. from a given URL like:
    'https://www.amazon.in' → 'amazon.in'
    """
    if "://" in url_or_domain:
        parsed = urlparse(url_or_domain)
        return parsed.netloc.replace("www.", "")
    return url_or_domain.replace("www.", "")

#
@router.get("/companies",status_code=status.HTTP_200_OK,response_model=list[ResponseData])
def list_company(db:Session=Depends(get_db)):
    return db.query(Company).all()


@router.post("/companies",status_code=status.HTTP_201_CREATED,response_model=ResponseData)
def add_company(data:CreateCompany,db:Session=Depends(get_db)):
    name=data.name
    website=extract_domain(str(data.website))
    funding_stage=data.funding_stage
    company=db.query(Company).filter(Company.website==website).first()
    if company:
        raise HTTPException(detail="Company already Listed",status_code=status.HTTP_409_CONFLICT)

    new_data=Company(name=name,website=website,funding_stage=funding_stage,created_at=datetime.now())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data