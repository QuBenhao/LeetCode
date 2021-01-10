import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        jobs, k = test_input
        return self.minimumTimeRequired(list(jobs), k)

    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
