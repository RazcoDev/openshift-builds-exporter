def nodes_json_to_names_list(node_json: dict) -> list:
    nodes_names_list = []
    for node in node_json['items']:
        nodes_names_list.append(node['metadata']['name'])
    return nodes_names_list
