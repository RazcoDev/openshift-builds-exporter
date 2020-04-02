from templates.buildconfig import BUILDCONFIG_TEMPLATE


def get_imagestreams_names_list(nodes_names_list: list) -> list:
    return [node_name + '-is' for node_name in nodes_names_list]


def get_formatted_buildconfig_template(buildconfig_name: str, namespace: str, imagestream_name,
                                       buildconfig_template: dict = BUILDCONFIG_TEMPLATE):
    buildconfig_template['metadata']['name'] = imagestream_name
    buildconfig_template['metadata']['namespace'] = namespace
    return buildconfig_template
