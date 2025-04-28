from sqlalchemy.orm import Session
from . import models, schemas

def add_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(
        project_name=project.project_name,
        client_group=project.client_group,
        added_by=project.added_by
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_all_projects(db: Session):
    return db.query(models.Project).all()

def get_projects_by_user(db: Session, added_by: str):
    return db.query(models.Project).filter(models.Project.added_by == added_by).all()
