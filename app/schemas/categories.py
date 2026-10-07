# schemas/categories.py
from pydantic import BaseModel, Field, ConfigDict

class SCategoryBase(BaseModel):
    pass

class SCategoryRead(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(from_attributes=True)

class SCategoryAdd(BaseModel):
    name: str = Field(min_length=1)

class SCategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1)

