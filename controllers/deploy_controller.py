from interfaces.openshift_api import Api
from handlers.deploymentconfigs import get_deployment
from utils.deployments import is_deployment_finished, get_finished_deploy_duration


async def get_deployments_list(openshift_api: Api, namespace: str, deploymentconfigs_names_list: list):
    res = []
    for deploymentconfig_name in deploymentconfigs_names_list:
        res.append(await get_deployment(openshift_api, namespace, deploymentconfig_name + '-1'))
    return res


async def get_deployments_results_json(openshift_api: Api, namespace: str, deployments_json_list: list) -> list:
    for idx, deployment in enumerate(deployments_json_list):
        result = await get_deployment(openshift_api, namespace, deployment['deploy_name'])
        deployments_json_list[idx]['result'] = is_deployment_finished(result)
    return deployments_json_list


async def get_deployments_duration_json_list(openshift_api: Api, namespace: str, deployments_json_list: list) -> list:
    for idx, deployment in enumerate(deployments_json_list):
        if deployments_json_list[idx]['result'] is True:
            result = await get_deployment(openshift_api, namespace, deployment['deploy_name'])
            deployments_json_list[idx]['result'] = get_finished_deploy_duration(result)
        else:
            deployments_json_list[idx]['result'] = -1
    return deployments_json_list
