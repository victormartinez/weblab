from typing import List
from uuid import UUID

from flask import Blueprint
from flask_pydantic import validate
from opentelemetry import trace

from .data import CUSTOMERS
from .schema import CustomerOut

app = Blueprint("customers", __name__)
tracer = trace.get_tracer(__name__)


@app.route("/customers", methods=["GET"])
@validate()
def list() -> List[CustomerOut]:
    with tracer.start_as_current_span("list-customers") as span:
        result = [
            CustomerOut(id=idx, **data).dict()
            for idx, data in CUSTOMERS.items()
        ]
        span.set_status(trace.Status(trace.StatusCode.OK))
        return result


@app.route("/customers/<id>", methods=["GET"])
@validate()
def detail(id: UUID) -> CustomerOut:
    data = CUSTOMERS.get(str(id))
    if data:
        return CustomerOut(id=id, **data)
    raise ValueError()
