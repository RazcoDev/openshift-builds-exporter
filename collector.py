from interfaces.openshift_api import Api
from handlers.nodes import get_nodes_names_list
from tasks.resource_init import delete_resources, create_resources
from tasks.builds import

async def collect(url, token, env_name, namespace):
    openshift_api = Api(url, token, env_name)
    nodes_names_list = await get_nodes_names_list(openshift_api)

    # Creating Imagestreams and then Buildconfigs for initial setup
    create_resources(openshift_api, namespace, nodes_names_list)

