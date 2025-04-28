from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from . import crud, schemas, database

router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add_project", response_model=schemas.ProjectResponse)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.add_project(db, project)

@router.get("/projects", response_model=List[schemas.ProjectResponse])
def read_projects(db: Session = Depends(get_db)):
    return crud.get_all_projects(db)

@router.get("/projects/by_user", response_model=List[schemas.ProjectResponse])
def read_projects_by_user(added_by: str = Query(...), db: Session = Depends(get_db)):
    return crud.get_projects_by_user(db, added_by)
