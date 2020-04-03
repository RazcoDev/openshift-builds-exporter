import asyncio
import aiohttp
from utils.aiofetch import fetch, Methods


class Api:
    def __init__(self, url, token, env_name):
        self.token = token
        self.name = env_name
        self.url = url

    def __repr__(self):
        return f'Api({self.name} , {self.url} , {self.token})'

    async def get_resource(self, api_route: str, verify: bool = False):
        endpoint = self._get_endpoint(api_route)
        headers = self._get_auth_header()

        return await fetch(method=Methods.GET, url=endpoint, verify=verify, headers=headers)

    async def create_resource(self, api_route: str, json_body: dict = None, verify: bool = False):
        endpoint = self._get_endpoint(api_route)
        headers = self._get_auth_header()
        return await fetch(method=Methods.POST, url=endpoint, verify=verify, headers=headers, json_body=json_body)

    async def delete_resource(self, api_route: str, json_body: dict = None, verify: bool = False):
        endpoint = self._get_endpoint(api_route)
        headers = self._get_auth_header()

        return await fetch(method=Methods.DELETE, url=endpoint, verify=verify, headers=headers, json_body=json_body)


    def _get_auth_header(self):
        return {"Authorization": 'Bearer {}'.format(self.token)}

    def _get_endpoint(self, api_route):
        return '{}{}'.format(self.url[:-1], api_route) if self.url[-1] == '/' else '{}{}'.format(self.url, api_route)
