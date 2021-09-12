from typing import List, Optional

from pydantic import BaseModel


class user_base(BaseModel):
    username : str
    password : str




class user_create(user_base):
    firstname : str
    lastname : str
    phone_number : Optional[str] = None
    gender : str

    class Config:
        orm_mode = True




class CreateFamily(BaseModel):
    parents_username: List[str]
    childs_username: List[str]

    class Config:
        orm_mode = True



class PackageSelection(BaseModel):
    child_username: str
    package_type: str

    class Config:
        orm_mode = True

class PackageDeletion(BaseModel):
    child_username: str

    class Config:
        orm_mode = True
   