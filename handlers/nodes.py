import json
from interfaces.openshift_api import Api
from config.urls import NODES_URL
from utils.nodes import nodes_json_to_names_list


async def get_nodes_names_list(openshift_api: Api) -> list:
    api_route = NODES_URL
    res = await openshift_api.get_resource(api_route)
    return nodes_json_to_names_list(json.loads(res))
