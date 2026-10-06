import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countMentions(*test_input)

    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # Sort by timestamp in ascending order; put offline events first when timestamps are equal
        events.sort(key=lambda e: (int(e[1]), e[0][2]))

        ans = [0] * numberOfUsers
        online_t = [0] * numberOfUsers
        for type_, timestamp, mention in events:
            cur_t = int(timestamp)  # Current time
            if type_[0] == 'O':  # Offline
                online_t[int(mention)] = cur_t + 60  # Next time online
            elif mention[0] == 'A':  # @everyone
                for i in range(numberOfUsers):
                    ans[i] += 1
            elif mention[0] == 'H':  # @all online users
                for i, t in enumerate(online_t):
                    if t <= cur_t:  # Online
                        ans[i] += 1
            else:  # @id
                for s in mention.split():
                    ans[int(s[2:])] += 1
        return ans
