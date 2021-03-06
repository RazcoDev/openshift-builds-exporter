from os import environ
from aioprometheus_thin import init_metrics, runner

from collector import collect
from metrics import CUSTOM_METRICS_LIST

PORT = environ.get('PORT')
HOST = environ.get('HOST')


def get_metrics_list(custom_metircs_list: list = CUSTOM_METRICS_LIST) -> list:
    return [init_metrics.Metric(v['name'], v['description'], v['metric_type'], v['const_labels'])
            for v in custom_metircs_list]


if __name__ == '__main__':
    metrics_list = get_metrics_list()
    runner.run_async(metrics_list, HOST, PORT, collect)



