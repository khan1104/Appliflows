from config.databse import Base
from sqlalchemy import Column,Integer,String,ForeignKey


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    name = Column(String)
    title = Column(String)
    email = Column(String)
    linkedin = Column(String)
    domain=Column(String)
