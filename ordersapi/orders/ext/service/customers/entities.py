from uuid import UUID

from pydantic import BaseModel


class Customer(BaseModel):
    id: UUID
    name: str
    surname: str
    email: str
