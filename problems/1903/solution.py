import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestOddNumber(str(test_input))

    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""
