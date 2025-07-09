from config.databse import Base
from sqlalchemy import Integer,String,Column,DateTime

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    website = Column(String)
    funding_stage = Column(String)
    created_at = Column(DateTime)