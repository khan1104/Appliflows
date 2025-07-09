from fastapi import APIRouter,status,Depends
from schemas.contact import ContactCreate
from sqlalchemy.orm import Session
from config.databse import get_db
from models.contacts import Contact
from models.company import Company
from typing import List


router=APIRouter()


@router.get("/contacts",status_code=status.HTTP_200_OK)
def list_contacts(db:Session=Depends(get_db)):
    return db.query(Contact).all()

@router.post("/webhooks/n8n-leads",status_code=status.HTTP_201_CREATED)
def add_contacts(data: List[ContactCreate], db: Session = Depends(get_db)):
    new_contacts = []
    for contact_data in data:
        company_data=db.query(Company).filter(Company.website==contact_data.domain).first()
        id=company_data.id
        contact = Contact(**contact_data.model_dump(),company_id=id)
        db.add(contact)
        new_contacts.append(contact)
    db.commit()
    for contact in new_contacts:
        db.refresh(contact)
    return new_contacts