from typing import Dict

from flask import Flask, jsonify

from customers.ext.opentelemetry.config import configure_tracer, configure_metric


def create_app(override_settings: Dict = None) -> Flask:
    app = minimal_app(override_settings)
    configure_blueprints(app)
    configure_routes(app)
    configure_error_handlers(app)
    return app


def minimal_app(override_settings: Dict = None) -> Flask:
    app = Flask(__name__)
    configure_app(app, override_settings)
    configure_extensions(app)
    return app


def configure_extensions(app: Flask) -> None:
    configure_tracer()
    configure_metric()


def configure_app(app: Flask, override_settings: Dict = None) -> None:
    from settings import APP_CONFIG

    app.config.update(**APP_CONFIG)

    if override_settings:
        app.config.update(**override_settings)


def configure_blueprints(app: Flask) -> None:
    from .api import resources

    app.register_blueprint(resources.app)


def configure_routes(app: Flask) -> None:
    app.add_url_rule(
        "/",
        view_func=lambda: jsonify(
            application="Customers API",
            health=True,
        ),
    )


def configure_error_handlers(app: Flask) -> None:
    pass
