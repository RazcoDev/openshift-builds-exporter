from aioprometheus_thin import init_metrics, runner
from aioprometheus_thin.configs import MetricsTypes
from collectors.build_metric import collector
import socket

const_labels = {'host': socket.gethostname()}
my_metrics = [
    {
        'name': 'shmuter_sum',
        'description': 'shmuter sum metric',
        'metric_type': MetricsTypes.summary,
        'const_labels': const_labels
    },
    {
        'name': 'raz_counter',
        'description': 'raz counter metric',
        'metric_type': MetricsTypes.counter,
        'const_labels': const_labels
    }
]

if __name__ == '__main__':
    metrics_list = [init_metrics.Metric(v['name'], v['description'], v['metric_type'], v['const_labels'])
                    for v in my_metrics]
    runner.run_async(metrics_list, '127.0.0.1', 5000, collector)
