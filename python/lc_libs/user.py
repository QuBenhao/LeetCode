import json
from typing import Optional

import requests

from python.constants import LEET_CODE_BACKEND, USER_PROFILE_PUBLIC_QUERY
from python.utils import general_request


def get_user_profile(user_slug: str) -> Optional[dict]:
    def handle_response(response: requests.Response):
        if not response.text:
            return
        result_dict = json.loads(response.text)['data']['userProfilePublicProfile']
        if not result_dict:
            return
        ans = dict()
        ans['name'] = result_dict['profile']['realName']
        ans['uid'] = result_dict['profile']['userSlug']
        ans['siteRanking'] = result_dict['siteRanking']
        ans['avatar'] = result_dict['profile']['userAvatar']
        return ans

    return general_request(LEET_CODE_BACKEND, handle_response,
                           json={"query": USER_PROFILE_PUBLIC_QUERY,
                                 "variables": {"userSlug": user_slug},
                                 "operationName": "userProfilePublicProfile"})


def check_user_exist(user_slug):
    return get_user_profile(user_slug) is not None
