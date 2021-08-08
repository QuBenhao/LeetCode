#!/usr/bin/env python3

import json
import requests

# 力扣目前勋章的配置
RATING = 1600
GUARDIAN = 0.05
KNIGHT = 0.25
# 二分查找的右端点(可自调)
RIGHT = 3000


class GlobalRankingCrawler:
    _REQUEST_PAYLOAD_TEMPLATE = {
        "operationName": None,
        "variables": {},
        "query":
r'''{
    globalRanking(page: 1) {
        totalUsers
        userPerPage
        rankingNodes {
            currentRating
            currentGlobalRanking
        }
    }
}
'''
    }

    def fetch_lastest_ranking(self, mode):
        l, r = 1, RIGHT
        retry_cnt = 0
        ansGlobalRanking = None
        while l < r:
            cur_page = (l + r + 1) // 2
            try:
                payload = GlobalRankingCrawler._REQUEST_PAYLOAD_TEMPLATE.copy()
                payload['query'] = payload['query'].replace('page: 1', 'page: {}'.format(cur_page))
                resp = requests.post('https://leetcode.com/graphql',
                    headers = {'Content-type': 'application/json'},
                    json = payload).json()

                resp = resp['data']['globalRanking']
                # no more data
                if len(resp['rankingNodes']) == 0:
                    break
                if not mode:
                    top = int(resp['rankingNodes'][0]['currentRating'].split('.')[0])
                    if top < RATING:
                        r = cur_page - 1
                    else:
                        l = cur_page
                        ansGlobalRanking = resp['rankingNodes']
                else:
                    top = int(resp['rankingNodes'][0]['currentGlobalRanking'])
                    if top > mode:
                        r = cur_page - 1
                    else:
                        l = cur_page
                        ansGlobalRanking = resp['rankingNodes']

                print('The first contest current rating in page {} is {} .'.format(cur_page, resp['rankingNodes'][0]['currentRating']))
                retry_cnt = 0
            except:
                # print(f'Failed to retrieved data of page {cur_page}...retry...{retry_cnt}')
                retry_cnt += 1
        ansGlobalRanking = ansGlobalRanking[::-1]
        last = None
        if not mode:
            while ansGlobalRanking and int(ansGlobalRanking[-1]['currentRating'].split('.')[0]) >= 1600:
                last = ansGlobalRanking.pop()
        else:
            while ansGlobalRanking and int(ansGlobalRanking[-1]['currentGlobalRanking']) <= mode:
                last = ansGlobalRanking.pop()
        return last


if __name__ == "__main__":
    crawler = GlobalRankingCrawler()
    ans = crawler.fetch_lastest_ranking(0)
    n = int(ans['currentGlobalRanking'])
    guardian = crawler.fetch_lastest_ranking(int(GUARDIAN * n))
    knight = crawler.fetch_lastest_ranking(int(KNIGHT * n))

    print("Done!")
    print()
    print("目前全球1600分以上的有{}人".format(n))
    print("根据这个人数，我们得到的Guardian排名及分数信息为:{}".format(guardian))
    print("根据这个人数，我们得到的Knight排名及分数信息为:{}".format(knight))
