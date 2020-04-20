import socket

from aioprometheus_thin.configs import MetricsTypes

CONST_LABELS = {'host': socket.gethostname()}
CUSTOM_METRICS_LIST = [
    {
        'name': 'builds_success_rate_gauge',
        'description': 'Builds success rate out of all builds.',
        'metric_type': MetricsTypes.gauge,
        'const_labels': CONST_LABELS
    },
    {
        'name': 'builds_complete_duration',
        'description': 'Builds completion duration, will marked as -1 if failed or incomplete',
        'metric_type': MetricsTypes.gauge,
        'const_labels': CONST_LABELS
    },
    {
        'name': 'deployments_complete_duration',
        'description': 'Deployments completion duration, will marked as -1 if failed or incomplete',
        'metric_type': MetricsTypes.gauge,
        'const_labels': CONST_LABELS
    },
    {
        'name': 'deployments_success_rate_gauge',
        'description': 'Deployments success rate out of all builds.',
        'metric_type': MetricsTypes.gauge,
        'const_labels': CONST_LABELS
    }
]
