import time
import asyncio
from interfaces.openshift_api import Api
from controllers.builds_controller import instantiate_builds, get_builds_duration_json_list, get_builds_results_json
from utils.buildconfigs import get_buildconfigs_names_list
from utils.builds import get_builds_json_list


async def build_task(openshift_api: Api, namespace: str, nodes_names_list: list, timeout: int, watch_sleep: int):
    buildconfigs_names_list = get_buildconfigs_names_list(nodes_names_list)
    instantiate_results = await instantiate_builds(openshift_api, namespace, buildconfigs_names_list)

    builds_json_list = await get_builds_json_list(instantiate_results)
    timeout_time = time.time() + timeout
    while True:
        print(timeout_time - time.time())
        if time.time() > timeout_time or all(build['result'] is True for build in builds_json_list):
            break
        builds_json_list = await get_builds_results_json(openshift_api, namespace, builds_json_list)
        await asyncio.sleep(watch_sleep)
    return await get_builds_duration_json_list(openshift_api, namespace, builds_json_list)

# TODO: Add master infras exclude
