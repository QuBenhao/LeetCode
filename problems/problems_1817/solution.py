import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findingUsersActiveMinutes(*test_input)

    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        d = defaultdict(set)
        for i,t in logs:
            d[i].add(t)
        ans = [0] * k
        for key in d:
            ans[len(d[key]) - 1] += 1
        return ans
