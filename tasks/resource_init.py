from interfaces.openshift_api import Api
from controllers.buildconfig_controller import create_buildconfigs, delete_buildconfigs
from controllers.imagestreams_controller import create_imagestreams, delete_imagestreams
from utils.buildconfigs import get_buildconfigs_names_list
from utils.imagestreams import get_imagestreams_names_list


def create_resources(openshift_api: Api, namespace: str, nodes_names_list: list) -> None:
    buildconfigs_names_list = get_buildconfigs_names_list(nodes_names_list)
    imagestreams_names_list = get_imagestreams_names_list(nodes_names_list)
    imagestreams_creation_res = create_imagestreams(openshift_api, namespace, imagestreams_names_list)
    buildconfigs_creation_res = create_buildconfigs(openshift_api, namespace, buildconfigs_names_list, nodes_names_list,
                                                    imagestreams_names_list)


def delete_resources(openshift_api: Api, namespace: str, nodes_names_list: list) -> None:
    buildconfigs_names_list = get_buildconfigs_names_list(nodes_names_list)
    imagestreams_names_list = get_imagestreams_names_list(nodes_names_list)
    imagestreams_deletion_res = delete_imagestreams(openshift_api, namespace, imagestreams_names_list)
    buildconfig_deletion_res = delete_buildconfigs(openshift_api, namespace, buildconfigs_names_list)
