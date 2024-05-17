import json
import traceback
import requests
from typing import Optional

from query import USER_PROFILE_PUBLIC_QUERY


def get_user_profile(user_slug: str) -> Optional[dict]:
    ans = None
    try:
        result = requests.post('https://leetcode.cn/graphql/',
                               json={"query": USER_PROFILE_PUBLIC_QUERY,
                                     "variables": {"userSlug": user_slug},
                                     "operationName": "userProfilePublicProfile"})
        if result.text:
            result_dict = json.loads(result.text)['data']['userProfilePublicProfile']
            if result_dict:
                ans = dict()
                ans['name'] = result_dict['profile']['realName']
                ans['uid'] = result_dict['profile']['userSlug']
                ans['siteRanking'] = result_dict['siteRanking']
                ans['avatar'] = result_dict['profile']['userAvatar']
    except Exception as e:
        print("Exception caught: ", str(e))
        traceback.print_exc()
    return ans


def check_user_exist(user_slug):
    return get_user_profile(user_slug) is not None


if __name__ == '__main__':
    print(check_user_exist("himymben"))
    print(check_user_exist("rearwassdgfvaswf"))
