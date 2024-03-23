import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.restoreString(*test_input)

    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res_str = [""] * len(s)
        for i in range(len(s)):
            res_str[indices[i]] = s[i]
        return "".join(res_str)
