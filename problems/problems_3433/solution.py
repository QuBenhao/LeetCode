import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countMentions(*test_input)

    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # 按照时间戳从小到大排序，时间戳相同的，离线事件排在前面
        events.sort(key=lambda e: (int(e[1]), e[0][2]))

        ans = [0] * numberOfUsers
        online_t = [0] * numberOfUsers
        for type_, timestamp, mention in events:
            cur_t = int(timestamp)  # 当前时间
            if type_[0] == 'O':  # 离线
                online_t[int(mention)] = cur_t + 60  # 下次在线时间
            elif mention[0] == 'A':  # @所有人
                for i in range(numberOfUsers):
                    ans[i] += 1
            elif mention[0] == 'H':  # @所有在线用户
                for i, t in enumerate(online_t):
                    if t <= cur_t:  # 在线
                        ans[i] += 1
            else:  # @id
                for s in mention.split():
                    ans[int(s[2:])] += 1
        return ans
