import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minDeletionSize(test_input)

    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return sum(1 if list(c) != sorted(c) else 0 for c in zip(*A))
