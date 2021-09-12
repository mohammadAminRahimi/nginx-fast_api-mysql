import fastapi
import uvicorn 

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register")
def register(usr: schemas.user_create, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, username=usr.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already exists")
    return crud.create_user(db=db, user=usr)


@app.post("/create-family")
def create_family(usr: schemas.CreateFamily, db: Session = Depends(get_db)):
    if ((len(usr.parents_username)==1 and len(usr.childs_username)<1) 
    or (len(usr.parents_username)<1)
    or (len(usr.parents_username)>2)):
        return "invalid request"
    if len(usr.parents_username)==2:
        if usr.parents_username[0] == usr.parents_username[1]:
            return "invalid request"
    family_id = crud.create_family(db, member_count=len(usr.parents_username)+len(usr.childs_username))
    users = list()
    for i in usr.parents_username:
        user = crud.get_user(db, username=i)
        user.parent_of = family_id
        users.append(user)
    for i in usr.childs_username:
        user = crud.get_user(db, username=i)
        user.child_of = family_id
        users.append(user)
    crud.update_users(db, users)
    return "succesfful operation"

@app.post("/package-selection")
def select_package(package_selection: schemas.PackageSelection, db: Session = Depends(get_db)):# selecting or changing package of a sonn
    package_type = crud.get_package(db, package_selection.package_type)
    user = crud.get_user(db, package_selection.child_username)
    user.pg = package_type
    ls = list()
    ls.append(user)
    crud.update_users(db, ls)
    return "selected successfully"
    

@app.post("/package-deletion")
def package_deletion(package_deletion: schemas.PackageDeletion, db: Session = Depends(get_db)):
    user = crud.get_user(db, package_deletion.child_username)
    print(type(user))
    print(user.username)
    user.pg = None
    ls = list()
    ls.append(user)
    crud.update_users(db, ls)
    return "deleted successfully"
