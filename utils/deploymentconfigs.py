from templates.deploymentconfig import DEPLOYMENTCONFIG_TEMPLATE


def get_formatted_deploymentconfigs_template(deploymentconfig_name: str, namespace: str, node_name: str,
                                             deploymentconfig_template: dict = DEPLOYMENTCONFIG_TEMPLATE) -> dict:
    deploymentconfig_template['metadata']['name'] = deploymentconfig_name
    deploymentconfig_template['metadata']['namespace'] = namespace
    deploymentconfig_template['spec']['template']['spec']['nodeSelector']['kubernetes.io/hostname'] = node_name
    return deploymentconfig_template

def get_deploymentconfig_names_list(nodes_names_list: list) -> list:
    return [node_name + '-dc' for node_name in nodes_names_list]
