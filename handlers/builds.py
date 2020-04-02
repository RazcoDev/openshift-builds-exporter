import json
from interfaces.openshift_api import Api
from config.urls import BUILD_URL, IMAGE_URL, INSTANTIATE_URL, INSTANTIATE_JSON


async def instantiate_build(openshift_api: Api, namespace: str, buildconfig: str) -> json:
    api_route = INSTANTIATE_URL.format(namespace, buildconfig)
    json_body = INSTANTIATE_JSON
    res = await openshift_api.create_resource(api_route, json_body)
    return json.loads(res)


async def watch_build(openshift_api: Api, namespace: str, build_name: str) -> json:
    api_route = BUILD_URL.format(namespace, build_name)
    res = await openshift_api.get_resource(api_route)
    return json.loads(res)


async def delete_image(openshift_api: Api, image_sha: str) -> json:
    api_route = IMAGE_URL.format(image_sha)
    res = await openshift_api.delete_resource(api_route)
    return json.loads(res)
