from sqlalchemy import Column,Index,String,Integer, Boolean, DateTime
from sqlalchemy import func
from db.database import Base

class Users(Base):

    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,index = True, nullable= False)
    password_hash = Column(String,nullable=False)
    is_active = Column(Boolean,default=True)
    is_verified = Column(Boolean,default=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )