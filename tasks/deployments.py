import time
import asyncio
from interfaces.openshift_api import Api
from controllers.deploy_controller import get_deployments_list, get_deployments_results_json, \
    get_deployments_duration_json_list
from utils.deploymentconfigs import get_deploymentconfig_names_list
from utils.deployments import get_deployments_json_list


async def deploy_task(openshift_api: Api, namespace: str, nodes_names_list: list, timeout: int, watch_sleep: int):
    deploymentconfigs_names_list = get_deploymentconfig_names_list(nodes_names_list)
    deployments_results = await get_deployments_list(openshift_api, namespace, deploymentconfigs_names_list)

    deployments_json_list = await get_deployments_json_list(deployments_results)
    timeout_time = time.time() + timeout
    while True:
        print(timeout_time - time.time())
        if time.time() > timeout_time or all(deployment['result'] is True for deployment in deployments_json_list):
            break
        deployments_json_list = await get_deployments_results_json(openshift_api, namespace, deployments_json_list)
        await asyncio.sleep(watch_sleep)
    return await get_deployments_duration_json_list(openshift_api, namespace, deployments_json_list)
