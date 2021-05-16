import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countVowelStrings(test_input)

    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for j in range(1,n+2):
            curr_sum = 0
            for i in range(1,j+1):
                curr_sum += i
                ans += curr_sum
        return ans
