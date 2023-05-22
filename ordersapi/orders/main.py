from typing import Any, Dict

from fastapi import FastAPI

from orders.ext.opentelemetry.config import configure_tracer, configure_metric

def create_application() -> FastAPI:
    application = FastAPI()
    configure_extensions()
    configure_healthcheck(application)
    configure_routes(application)
    return application


def configure_extensions() -> None:
    configure_tracer()
    configure_metric()


def configure_routes(app: FastAPI) -> None:
    from orders.api.resources import router as orders_router

    app.include_router(orders_router)


def configure_healthcheck(app: FastAPI) -> None:
    @app.get("/")
    async def healthcheck() -> Dict[str, Any]:
        return {
            "application": "Orders API",
            "healthy": True,
        }


app = create_application()
