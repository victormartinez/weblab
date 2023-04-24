from typing import Dict

from flask import Flask, jsonify

from .ext import configure_extensions


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


def configure_app(app: Flask, override_settings: Dict = None) -> None:
    from settings import APP_CONFIG

    app.config.update(**APP_CONFIG)

    if override_settings:
        app.config.update(**override_settings)


def configure_blueprints(app: Flask) -> None:
    from . import BLUEPRINTS

    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def configure_routes(app: Flask) -> None:
    app.add_url_rule(
        "/",
        view_func=lambda: jsonify(
            application="myflaskapi",
            health=True,
        ),
    )


def configure_error_handlers(app: Flask) -> None:
    pass
