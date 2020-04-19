import asyncio
from os import environ

from controllers.nodes_controller import get_nodes_names_list_by_labels
from interfaces.openshift_api import Api
from tasks.builds import build_task
from tasks.resource_init import delete_resources, create_resources
from utils.metrics import update_build_duration_metric, update_success_rate_metric

ENV_URL = environ.get('ENV_URL')
DEFAULT_TOKEN = environ.get('DEFAULT_TOKEN')
ENV_NAME = environ.get('ENV_NAME')
NAMESPACE = environ.get('OPENSHIFT_BUILD_NAMESPACE')
TIMEOUT = environ.get('TIMEOUT')
WATCH_SLEEP = environ.get('WATCH_SLEEP')
COLLECT_INTERVAL = environ.get('COLLECT_INTERVAL')
LABEL_NAME = environ.get('LABEL_NAME')
LABEL_VALUE = environ.get('LABEL_VALUE')

async def collect(metrics_list: list) -> None:
    url = ENV_URL
    token = DEFAULT_TOKEN
    env_name = ENV_NAME
    namespace = NAMESPACE
    timeout = int(TIMEOUT)
    watch_sleep = int(WATCH_SLEEP)
    collect_inetrval = int(COLLECT_INTERVAL)

    success_rate_metric = metrics_list[0]
    build_duration_metric = metrics_list[1]
    while True:
        openshift_api = Api(url, token, env_name)
        nodes_names_list = await get_nodes_names_list_by_labels(openshift_api, LABEL_NAME,LABEL_VALUE)

        # Creating Imagestreams and then Buildconfigs for initial setup
        await create_resources(openshift_api, namespace, nodes_names_list)

        # Getting results from builds
        results_json_list = await build_task(openshift_api, namespace, nodes_names_list, timeout, watch_sleep)

        # Deleting Imagestreams and Buildconfigs
        await delete_resources(openshift_api, namespace, nodes_names_list, results_json_list)
        print(results_json_list)

        update_build_duration_metric(build_duration_metric, results_json_list)
        update_success_rate_metric(success_rate_metric, results_json_list)

        await asyncio.sleep(collect_inetrval)


# def build_and_deploy_task()