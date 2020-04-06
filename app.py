from aioprometheus_thin import init_metrics, runner
from metrics import CUSTOM_METRICS_LIST
from collector import collect
import socket


def get_metrics_list(custom_metircs_list: list = CUSTOM_METRICS_LIST) -> list:
    return [init_metrics.Metric(v['name'], v['description'], v['metric_type'], v['const_labels'])
            for v in custom_metircs_list]


if __name__ == '__main__':
    metrics_list = get_metrics_list()
    runner.run_async(metrics_list, '127.0.0.1', 5000, collect)



