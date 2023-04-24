from .main import create_app
from .customers import app as customers_app

BLUEPRINTS = [
    customers_app,
]
