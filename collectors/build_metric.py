import asyncio
from interfaces.openshift_api import Api
from controllers.build_actions import instantiate_build, watch_build, delete_image


async def collector(metric_list: list, time_await: int, openshift_url: str, openshift_token: str,
                    openshift_env_name: str) -> None:
    while True:
        openshift_api = Api(url=openshift_url, token=openshift_token, name=openshift_env_name)

        await asyncio.sleep(time_await)
