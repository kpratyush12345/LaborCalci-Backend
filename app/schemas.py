from pydantic import BaseModel

class ProjectCreate(BaseModel):
    project_name: str
    client_group: str
    added_by: str

class ProjectResponse(BaseModel):
    id: int
    project_name: str
    client_group: str
    added_by: str

    class Config:
        from_attributes = True
