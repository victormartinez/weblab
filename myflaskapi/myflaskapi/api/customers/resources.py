from typing import List
from uuid import UUID

from flask import Blueprint
from flask_pydantic import validate

from .data import CUSTOMERS
from .schema import CustomerOut

app = Blueprint("customers", __name__)


@app.route("/customers", methods=["GET"])
@validate()
def list() -> List[CustomerOut]:
    return [
        CustomerOut(id=idx, **data).dict()
        for idx, data in CUSTOMERS.items()
    ]


@app.route("/customers/<id>", methods=["GET"])
@validate()
def detail(id: UUID) -> CustomerOut:
    data = CUSTOMERS.get(str(id))
    if data:
        return CustomerOut(id=id, **data)
    raise ValueError()
