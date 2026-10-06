# schemas/tasks.py
from pydantic import BaseModel, ConfigDict, Field

class STaskBase(BaseModel):
    title: str | None = Field(default=None, min_length=1)

class STaskRead(STaskBase):
    id: str
    title: str
    completed: bool

    model_config = ConfigDict(from_attributes=True)

class STaskAdd(STaskBase):
    title: str = Field(min_length=1)

class STaskUpdate(STaskBase):
    completed: bool | None = None