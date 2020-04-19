import json

from config.urls import DEPLOYMENTCONFIG_URL, DEPLOYMENT_URL
from interfaces.openshift_api import Api


async def create_deploymentconfig(openshift_api: Api, namespace: str, deploymentconfig_template: json) -> json:
    api_route = DEPLOYMENTCONFIG_URL.format(namespace, '')
    res = await openshift_api.create_resource(api_route, deploymentconfig_template)
    return json.loads(res)


async def delete_deploymentconfig(openshift_api: Api, namespace: str, deploymentconfig_name: str) -> json:
    api_route = DEPLOYMENTCONFIG_URL.format(namespace, deploymentconfig_name)
    res = await openshift_api.delete_resource(api_route)
    return json.loads(res)


async def delete_deployment(openshift_api: Api, namespace: str, deployment_name: str) -> json:
    api_route = DEPLOYMENT_URL.format(namespace, deployment_name)
    res = await  openshift_api.delete_resource(api_route)
    return json.loads(res)
