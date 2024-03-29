import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestMerge(*test_input)

    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = ""
        while word1:
            if not word2:
                ans += word1
                return ans
            if word1 > word2:
                word1, word2 = word2, word1
            ans += word2[0]
            word2 = word2[1:]
        return ans
