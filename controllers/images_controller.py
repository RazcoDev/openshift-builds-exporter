from interfaces.openshift_api import Api
from handlers.builds import watch_build, delete_image


async def delete_images(openshift_api: Api, namespace: str, completed_builds_list: list):
    res = []
    for completed_build in completed_builds_list:
        image_sha = await get_image_sha(openshift_api, namespace, completed_build)
        res.append(await delete_image(openshift_api, image_sha))

    return res


async def get_image_sha(openshift_api: Api, namespace: str, build_name: str) -> str:
    build_result = await watch_build(openshift_api, namespace, build_name)
    return build_result['status']['output']['to']['imageDigest']
