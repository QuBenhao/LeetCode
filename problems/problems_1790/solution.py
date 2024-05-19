import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.areAlmostEqual(*test_input)

    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        diff = [[c1, c2] for c1,c2 in zip(s1, s2) if c1 != c2]
        return not diff or (len(diff) == 2 and diff[0][::-1] == diff[1])
