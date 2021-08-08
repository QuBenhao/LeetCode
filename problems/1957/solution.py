import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.makeFancyString(str(test_input))

    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        q = []
        count = 0
        for c in s:
            if q and c == q[-1]:
                count += 1
            else:
                count = 1
            if count < 3:
                q.append(c)
        return ''.join(q)
