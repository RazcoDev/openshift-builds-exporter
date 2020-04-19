from interfaces.openshift_api import Api
from handlers.deploymentconfigs import delete_deployment


async def delete_deployments(openshift_api: Api, namespace: str, deploymentconfig_names_list: str):
    res = []
    for deploymentconfig_name in deploymentconfig_names_list:
        res.append(await delete_deployment(openshift_api,namespace, deploymentconfig_name+'-1'))

    return res
