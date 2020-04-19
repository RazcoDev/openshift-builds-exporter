from interfaces.openshift_api import Api
from handlers.nodes import get_nodes_json


async def get_nodes_names_list_by_labels(openshift_api: Api, label_name, label_value) -> list:
    nodes_json = await get_nodes_json(openshift_api)
    nodes_names_list = []
    for idx, node in enumerate(nodes_json['items']):
        is_label_valid = True
        if label_name in node['metadata']['labels']:
            if node['metadata']['labels'][label_name] != label_value:
                is_label_valid = False
        else:
            is_label_valid = False

        if is_label_valid:
            nodes_names_list.append(node['metadata']['name'])
    return nodes_names_list
