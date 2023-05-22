from typing import List
from uuid import UUID

from pydantic import BaseModel


class CustomerOut(BaseModel):
    id: UUID
    name: str
    surname: str
    email: str


class OrderOut(BaseModel):
    id: UUID
    title: str


class OrdersOut(BaseModel):
    customer: CustomerOut
    orders: List[OrderOut]

