import json
import traceback
import requests
from typing import Optional


def get_user_profile(user_slug: str) -> Optional[dict]:
    ans = None
    try:
        result = requests.post('https://leetcode.cn/graphql/',
                               json={"query": "\n    query userProfilePublicProfile($userSlug: String!) {\n  "
                                              "userProfilePublicProfile(userSlug: $userSlug) {\n    haveFollowed\n    "
                                              "siteRanking\n    profile {\n      userSlug\n      realName\n      "
                                              "aboutMe\n      asciiCode\n      userAvatar\n      gender\n      "
                                              "websites\n      skillTags\n      ipRegion\n      birthday\n      "
                                              "location\n      useDefaultAvatar\n      github\n      "
                                              "school: schoolV2 {\n        schoolId\n        logo\n        name\n      "
                                              "}\n      company: companyV2 {\n        id\n        logo\n        name\n"
                                              "      }\n      job\n      globalLocation {\n        country\n        "
                                              "province\n        city\n        overseasCity\n      }\n      "
                                              "socialAccounts {\n        provider\n        profileUrl\n      }\n      "
                                              "skillSet {\n        langLevels {\n          langName\n          "
                                              "langVerboseName\n          level\n        }\n        topics {\n     "
                                              "     slug\n          name\n          translatedName\n        }\n        "
                                              "topicAreaScores {\n          score\n          topicArea {\n            "
                                              "name\n            slug\n          }\n        }\n      }\n    }\n    "
                                              "educationRecordList {\n      unverifiedOrganizationName\n    }\n    "
                                              "occupationRecordList {\n      unverifiedOrganizationName\n      "
                                              "jobTitle\n    }\n  }\n}\n    ",
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
