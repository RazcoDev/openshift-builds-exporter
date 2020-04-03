from interfaces.openshift_api import Api
from handlers.nodes import get_nodes_names_list
from tasks.resource_init import delete_resources, create_resources
from tasks.builds import build_task


async def collect(url, token, env_name, namespace):
    openshift_api = Api(url, token, env_name)
    nodes_names_list = await get_nodes_names_list(openshift_api)

    # Creating Imagestreams and then Buildconfigs for initial setup
    # await create_resources(openshift_api, namespace, nodes_names_list)

    # Getting results from builds
    results_json_list = await build_task(openshift_api, namespace, nodes_names_list, 300, 10)

    # Deleting Imagestreams and Buildconfigs
    # await delete_resources(openshift_api, namespace, nodes_names_list)

    print(results_json_list)
