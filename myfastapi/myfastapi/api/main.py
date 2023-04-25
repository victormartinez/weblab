from typing import Any, Dict

from fastapi import FastAPI
from opentelemetry import trace

from myfastapi.api.ext import configure_extensions


tracer = trace.get_tracer(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    configure_extensions(application)
    configure_healthcheck(application)
    configure_routes(application)

    return application


def configure_routes(app: FastAPI) -> None:
    pass


def configure_healthcheck(app: FastAPI) -> None:
    @app.get("/")
    async def healthcheck() -> Dict[str, Any]:
        with tracer.start_as_current_span("healthcheck") as span:
            span.set_attribute("application.name", "my fastapi")
            return {
                "application": "My FastAPI",
                "healthy": True,
            }


app = create_application()
