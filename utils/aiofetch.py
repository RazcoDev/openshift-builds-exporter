import aiohttp
from enum import Enum


class Methods(Enum):
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'


async def fetch(method: Methods, url: str, verify: bool = True, headers: dict = None, json_body: dict = None):
    """
    :param method:
    :param headers:
    :param verify:
    :param url:
    :return: response from fething GET method
    """
    return await _set_session(method, url, verify, headers, json_body)


async def _set_session(method: Enum, url: str, verify: bool = True, headers: dict = None, json_body: dict = None):
    """
    This function sets ClientSession and pass it to _fetch function.
    :param method:
    :param url:
    :return: response from fetch
    """
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=verify)) as session:
        res = await _fetch(method, session, url, headers, json_body)
        return res


async def _fetch(method: Enum, session: aiohttp.ClientSession, url: str, headers: dict = None, json_body: dict = None):
    """
    This function fetch the response from the Client Session by the given method.
    :param method:
    :param session:
    :param url:
    :return:
    """
    response = None

    async with session.request(method.value, url, headers=headers, json=json_body) as res:
        if res.status in (200, 201):
            print(res.status)
        return await res.text()
