from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


class CustomerOut(BaseModel):
    id: UUID
    name: str
    surname: str
    email: str
