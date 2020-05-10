from handlers.deploymentconfigs import create_deploymentconfig, delete_deploymentconfig
from interfaces.openshift_api import Api
from utils.deploymentconfigs import get_formatted_deploymentconfigs_template


async def create_deploymentconfigs(openshift_api: Api, namespace: str, deploymentconfigs_names_list: list,
                                  nodes_names_list: list) -> list:
    res = []
    for deploymentconfig_name, node_name in zip(deploymentconfigs_names_list, nodes_names_list):
        deploymentconfig_template = get_formatted_deploymentconfigs_template(deploymentconfig_name, namespace,
                                                                             node_name)
        res.append(await create_deploymentconfig(openshift_api, namespace, deploymentconfig_template))
    return res


async def delete_deploymentconfigs(openshift_api: Api, namespace: str, deploymentconfigs_names_list: list) -> list:
    res = []
    for deploymentconfig_name in deploymentconfigs_names_list:
        res.append(await delete_deploymentconfig(openshift_api, namespace, deploymentconfig_name))
    return res
