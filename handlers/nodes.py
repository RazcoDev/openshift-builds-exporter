import json
from interfaces.openshift_api import Api
from config.urls import NODES_URL


async def get_nodes_json(openshift_api: Api) -> json:
    api_route = NODES_URL
    res = await openshift_api.get_resource(api_route)
    return json.loads(res)
