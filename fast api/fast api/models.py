from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class package(Base):
    __tablename__ = "package"
    type = Column("type", String(1), primary_key=True)
    description = Column("description", String(150))

class family(Base):
    __tablename__ = "family"
    family_id = Column("family_id", Integer, primary_key=True)
    member_count = Column("member_count", Integer)
    # parents = relationship("user", back_populates="parent_of1")
    # childs = relationship("user", back_populates="child_of1")

class user(Base):
    __tablename__ = "user"

    username = Column("username", String(30), primary_key=True, unique=True)
    password = Column("password", String(100), nullable=False)
    firstname = Column("firstname", String(30), nullable=False)
    lastname = Column("lastname",  String(30), nullable=False)
    phone_number = Column("phone_number", String(16))
    gender = Column("gender", String(5), nullable=False)
    pg = Column("pg",String(1),  ForeignKey("package.type", ondelete="SET NULL"))
    parent_of = Column("parent_of", Integer,  ForeignKey("family.family_id", ondelete="SET NULL"))
    child_of = Column("child_of", Integer,  ForeignKey("family.family_id", ondelete="SET NULL"))
    # parent_of1  = relationship("family", back_populates="parents")
    # child_of1 = relationship("family", back_populates="childs")

