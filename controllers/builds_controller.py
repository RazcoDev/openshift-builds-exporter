from interfaces.openshift_api import Api
from handlers.builds import instantiate_build, watch_build


def instantiate_builds(openshift_api: Api, namespace: str, buildconfigs_names_list: list):
    res = []
    for buildconfig_name in buildconfigs_names_list:
        res.append(await instantiate_build(openshift_api, namespace, buildconfig_name))
    return res


def get_builds_results_list(openshift_api: Api, namespace: str, builds_names_list: list) -> list:
    results_list = []
    for build_name in builds_names_list:
        results_list.append(await watch_build(openshift_api, namespace, build_name))
    for result in results_list:
        results_list.append(is_build_finished(result))
    return res
