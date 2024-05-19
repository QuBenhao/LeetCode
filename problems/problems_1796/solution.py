import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.secondHighest(str(test_input))

    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        li = sorted(list(set([int(c) for c in s if '0' <= c <= '9'])))
        return li[-2] if len(li) > 1 else -1
