from typing import Any, Dict

from fastapi import FastAPI


def create_application() -> FastAPI:
    application = FastAPI()
    configure_healthcheck(application)
    configure_routes(application)

    return application


def configure_routes(app: FastAPI) -> None:
    pass


def configure_healthcheck(app: FastAPI) -> None:
    @app.get("/")
    async def healthcheck() -> Dict[str, Any]:
        return {
            "application": "My FastAPI",
            "healthy": True,
        }


app = create_application()
