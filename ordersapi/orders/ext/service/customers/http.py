import json
from typing import List, Tuple, Type, Optional
from urllib.parse import urljoin
from uuid import UUID

import aiohttp
from pydantic import BaseModel

import settings
from orders.ext.service.customers.entities import Customer


def _create_session() -> aiohttp.ClientSession:
    timeout = aiohttp.ClientTimeout(
        total=settings.CUSTOMERS_SVC_TOTAL_TIMEOUT,
        connect=settings.CUSTOMERS_SVC_CONN_TIMEOUT,
    )
    return aiohttp.ClientSession(timeout=timeout)


async def _parse_response(response: aiohttp.ClientResponse, Model: Type[BaseModel], many=False) -> Optional[BaseModel]:
    try:
        content: bytes = await response.content.read()
        result = json.loads(content)
        return (
            [Model.parse_obj(o) for o in result]
            if many else Model.parse_obj(result)
        )
    except json.JSONDecodeError:
        return None


async def list_customers() -> Tuple[aiohttp.ClientResponse, List[Customer]]:
    url = urljoin(settings.CUSTOMERS_SVC_HOST, "/customers")
    async with _create_session() as session:
        async with session.get(url) as resp:
            return await _parse_response(resp, Customer, many=True)


async def get_customer(idx: UUID) -> Tuple[aiohttp.ClientResponse, Customer]:
    url = urljoin(settings.CUSTOMERS_SVC_HOST, f"/customers/{idx}")
    async with _create_session() as session:
        async with session.get(url) as resp:
            return await _parse_response(resp, Customer)
