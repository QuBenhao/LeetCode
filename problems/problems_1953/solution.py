import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfWeeks(list(test_input))

    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        m, s = max(milestones), sum(milestones)
        return (s - m) * 2 + 1 if m > s - m else s
