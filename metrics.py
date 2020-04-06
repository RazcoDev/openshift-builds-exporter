import socket

from aioprometheus_thin.configs import MetricsTypes

CONST_LABELS = {'host': socket.gethostname()}
CUSTOM_METRICS_LIST = [
    {
        'name': 'build_success_rate_gauge',
        'description': 'Build success rate out of all builds.',
        'metric_type': MetricsTypes.gauge,
        'const_labels': CONST_LABELS
    },
    {
        'name': 'build_complete_duration',
        'description': 'Build completion duration, will marked as -1 if failed or incomplete',
        'metric_type': MetricsTypes.gauge,
        'const_labels': CONST_LABELS
    }
]
