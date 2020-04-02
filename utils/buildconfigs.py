from templates.buildconfig import BUILDCONFIG_TEMPLATE


def get_buildconfigs_names_list(nodes_names_list: list) -> list:
    return [node_name + '-bc' for node_name in nodes_names_list]


def get_formatted_buildconfig_template(buildconfig_name: str, namespace: str, imagestream_name: str, node_name: str,
                                       buildconfig_template: dict = BUILDCONFIG_TEMPLATE) -> dict:
    buildconfig_template['metadata']['name'] = buildconfig_name
    buildconfig_template['metadata']['namespace'] = namespace
    buildconfig_template['spec']['nodeSelector']['kubernetes.io/hostname'] = node_name
    buildconfig_template['spec']['output']['to']['name'] = imagestream_name + ':latest'
    return buildconfig_template
