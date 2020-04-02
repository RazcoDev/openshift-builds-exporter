import json

from interfaces.openshift_api import Api
from config.urls import IMAGESTREAM_URL


async def create_imagestream(openshift_api: Api, namespace: str, imagestream_template: json) -> json:
    api_route = IMAGESTREAM_URL.format(namespace, None)
    res = await openshift_api.create_resource(api_route, imagestream_template)
    return json.loads(res)


async def delete_imagestream(openshift_api: Api, namespace: str, imagestream_name: str) -> json:
    api_route = IMAGESTREAM_URL.format(namespace, imagestream_name)
    res = await openshift_api.delete_resource(api_route)
    return json.loads(res)
