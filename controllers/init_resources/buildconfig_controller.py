from handlers.buildconfigs import create_buildconfig, delete_buildconfig
from interfaces.openshift_api import Api
from utils.buildconfigs import get_formatted_buildconfig_template


def create_buildconfigs(openshift_api: Api, namespace: str, buildconfigs_names_list: list,
                        nodes_names_list: list, imagestreams_names_list) -> list:
    res = []
    for buildconfig_name, node_name, imagestream_name in zip(buildconfigs_names_list, nodes_names_list,
                                                             imagestreams_names_list):
        buildconfig_template = get_formatted_buildconfig_template(buildconfig_name, node_name, imagestream_name,
        namespace)
        res.append(create_buildconfig(openshift_api, namespace, buildconfig_template))
    return res


def delete_buildconfigs(openshift_api: Api, namespace: str, imagestreams_names_list: list) -> list:
    res = []
    for imagestream_name in imagestreams_names_list:
        res.append(delete_imagestream(openshift_api, namespace, imagestream_name))

    return res
