from interfaces.openshift_api import Api
from handlers.builds import instantiate_build, watch_build
from utils.builds import is_build_finished, get_finished_build_duration


async def instantiate_builds(openshift_api: Api, namespace: str, buildconfigs_names_list: list):
    res = []
    for buildconfig_name in buildconfigs_names_list:
        res.append(await instantiate_build(openshift_api, namespace, buildconfig_name))
    return res


async def get_builds_results_json(openshift_api: Api, namespace: str, builds_json_list: list) -> list:
    for idx, build in enumerate(builds_json_list):
        result = await watch_build(openshift_api, namespace, build['build_name'])
        builds_json_list[idx]['result'] = is_build_finished(result)
    return builds_json_list


async def get_builds_duration_json_list(openshift_api: Api, namespace: str, builds_json_list: list) -> list:
    for idx, build in enumerate(builds_json_list):
        if builds_json_list[idx]['result'] is True:
            result = await watch_build(openshift_api, namespace, build['build_name'])
            builds_json_list[idx]['result'] = get_finished_build_duration(result)
        else:
            builds_json_list[idx]['result'] = -1
    return builds_json_list
