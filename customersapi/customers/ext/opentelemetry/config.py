from opentelemetry import trace, metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor


tracer = trace.get_tracer(__name__)
_SERVICE_NAME = "orders-api"


def configure_tracer():
    pass
    #provider = TracerProvider(
        #resource=Resource.create({SERVICE_NAME: _SERVICE_NAME})
    #)
    #provider.add_span_processor(span_processor)
    #trace.set_tracer_provider(provider)


def configure_metric():
    pass
    #from prometheus_client import start_http_server
    #resource = Resource(attributes={SERVICE_NAME: _SERVICE_NAME})
#
    #start_http_server(port=8000, addr="localhost")
    #reader = PrometheusMetricReader()
    #provider = MeterProvider(resource=resource, metric_readers=[reader])
    #metrics.set_meter_provider(provider)
