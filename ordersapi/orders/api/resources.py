from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter
from opentelemetry import trace, metrics

from orders.ext.service import customers
from orders.api.schema import (
    CustomerOut,
    OrdersOut,
    OrderOut,
)

router = APIRouter(tags=["orders"])
tracer = trace.get_tracer(__name__)
metric = metrics.get_meter(__name__)


@router.get(
    "/customers/{customer_id}/orders",
    response_model=OrdersOut,
    status_code=HTTPStatus.OK,
)
async def get_orders_by_customer(
    customer_id: UUID,
) -> OrdersOut:
    with tracer.start_as_current_span("ordersapi.get.orders.by.customer") as span:
        _, customer = await customers.get_customer(customer_id)
        span.set_attribute("total.orders", 0)
        span.set_status(status=trace.StatusCode.OK)

        return OrdersOut(
            customer=CustomerOut(**customer.dict()),
            orders=[]
        )
