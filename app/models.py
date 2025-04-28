from sqlalchemy import Column, Integer, String
from .database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, nullable=False)
    client_group = Column(String, nullable=False)
    added_by = Column(String, nullable=False)
