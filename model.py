from pydantic import BaseModel
from typing import Optional


class ToDo(BaseModel):
    id: Optional[str] = ''  # We will generate UUIDs by ourselves!
    title: str
    description: str
