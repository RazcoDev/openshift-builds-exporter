import json

from config.urls import BUILDCONFIG_URL
from interfaces.openshift_api import Api


async def create_buildconfig(openshift_api: Api, namespace: str, buildconfig_template: json) -> json:
    api_route = BUILDCONFIG_URL.format(namespace, None)
    res = await openshift_api.create_resource(api_route, buildconfig_template)
    return json.loads(res)


async def delete_buildconfig(openshift_api: Api, namespace: str, buildconfig_name: str) -> json:
    api_route = BUILDCONFIG_URL.format(namespace, buildconfig_name)
    res = await openshift_api.delete_resource(api_route)
    return json.loads(res)
