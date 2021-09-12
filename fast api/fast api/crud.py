from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user
from . import models, schemas


def create_user(db: Session, user: schemas.user_create):
    db_user = models.user(
        username=user.username, 
        password=user.password, 
        firstname = user.firstname,
        lastname = user.lastname, 
        gender = user.gender)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, username: str):
    return db.query(models.user).filter(models.user.username == username).first()


def update_users(db: Session, users):
    db.add_all(users)
    db.commit()
    return "updated"


def create_family(db: Session, member_count: int):
    family = models.family(member_count=member_count)
    db.add(family)
    db.commit()
    db.refresh(family)
    return family.family_id


def get_package(db, package_type: str):
    return db.query(models.package).filter(models.package.type == package_type).first().type

