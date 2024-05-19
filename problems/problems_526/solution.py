import solution
from collections import defaultdict
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countArrangement(test_input)

    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        canFill = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # 每个位置可以填入哪些数
                if j % i == 0 or i % j == 0:
                    canFill[i].append(j - 1)
        # 根据可填入数字的个数排序，优先填入个数少的
        order = sorted(canFill.keys(), key=lambda x: len(canFill[x]))
        end = (1 << n) - 1

        @lru_cache(None)
        def dfs(state):
            # 全部填入
            if state == end:
                return 1
            cnts = ans = 0
            # 当前该填第几个位置
            for i in range(n):
                if (1 << i) & state:
                    cnts += 1
            # 当前位置可以填哪些数
            for i in canFill[order[cnts]]:
                # 哪些数还没被填
                if not ((1 << i) & state):
                    ans += dfs(state ^ (1 << i))
            return ans

        return dfs(0)
