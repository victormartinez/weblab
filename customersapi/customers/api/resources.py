from typing import List
from uuid import UUID

from flask import Blueprint
from flask_pydantic import validate
from opentelemetry import trace

from customers.api.schema import CustomerOut


app = Blueprint("customers", __name__)
tracer = trace.get_tracer(__name__)

_CUSTOMERS = {
	"2c62ada0-e29c-11ed-b5ea-0242ac120002": {
		"name": "Reuben",
		"surname": "Hall",
		"email": "nulla.semper@aol.couk"
	},
	"2c62b052-e29c-11ed-b5ea-0242ac120002": {
		"name": "Kimberley",
		"surname": "Todd",
		"email": "dolor.donec.fringilla@yahoo.edu"
	},
	"2c62b19c-e29c-11ed-b5ea-0242ac120002": {
		"name": "Sarah",
		"surname": "Mullins",
		"email": "orci.in.consequat@protonmail.com"
	},
	"2c62b2c8-e29c-11ed-b5ea-0242ac120002": {
		"name": "Sophia",
		"surname": "Goodwin",
		"email": "ultricies.dignissim@protonmail.ca"
	},
	"2c62b3ea-e29c-11ed-b5ea-0242ac120002": {
		"name": "Sade",
		"surname": "Johnston",
		"email": "luctus.ut@google.net"
	}
}


@app.route("/customers", methods=["GET"])
@validate()
def list() -> List[CustomerOut]:
    with tracer.start_as_current_span("customersapi.list.customers") as span:
        result = [
            CustomerOut(id=idx, **data).dict()
            for idx, data in _CUSTOMERS.items()
        ]
        span.set_status(trace.Status(trace.StatusCode.OK))
        span.add_event("Successful result")
        return result


@app.route("/customers/<id>", methods=["GET"])
@validate()
def detail(id: UUID) -> CustomerOut:
    data = _CUSTOMERS.get(str(id))
    if data:
        return CustomerOut(id=id, **data)
    raise ValueError()
