from pydantic import BaseModel
from typing import Optional


class ToDo(BaseModel):
    id: Optional[str] = ''
    title: str
    description: str
