import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        batchSize, groups = test_input
        return self.maxHappyGroups(batchSize, list(groups))

    def maxHappyGroups(self, batchSize, groups):
        """
        :type batchSize: int
        :type groups: List[int]
        :rtype: int
        """
        remains = [0] * batchSize
        for g in groups:
            remains[g % batchSize] += 1
        ans = remains[0]
        remains[0] = 0
        # 贪心: 余数和为batchSize的可以两两一组
        for i in range(1, batchSize // 2 + 1):
            if i != batchSize - i:
                tp = min(remains[i], remains[batchSize - i])
                ans += tp
                remains[i] -= tp
                remains[batchSize - i] -= tp
            # 中间数
            else:
                ans += remains[i] // 2
                remains[i] %= 2

        # 之前人们的和的余数和剩余的人们
        @lru_cache(None)
        def dfs(s, remain):
            res = 0
            for i in range(1, batchSize):
                # 还有模batchSize余i的组
                if remain[i-1]:
                    r = list(remain)
                    r[i-1] -= 1
                    # 如果之前和的余数为0，开心的人数为dfs的结果+1；否则为dfs的结果
                    res = max(res, (s == 0) + dfs((s+i) % batchSize, tuple(r)))
            # 不在这里加上(s==0)是因为可能remain已经空了
            return res

        return ans + dfs(0, tuple(remains[1:]))
