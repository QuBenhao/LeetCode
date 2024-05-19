import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumEffort([x[:] for x in test_input])

    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda x:(x[1] - x[0]))
        res = 0
        for c,m in tasks:
            res = max(res + c, m)
        return res
