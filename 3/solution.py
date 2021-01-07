import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lengthOfLongestSubstring(str(test_input))

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # two pointer solution
        i = ans = 0
        index_dict = dict()

        for j in range(len(s)):
            if s[j] in index_dict:
                i = max(i,index_dict[s[j]])

            ans = max(ans, j - i + 1)
            index_dict[s[j]] = j + 1
        return ans

        # window = []
        # ans = 0
        # for c in s:
        #     while window and c in window:
        #         window.pop(0)
        #     window.append(c)
        #     ans = max(ans, len(window))
        # return ans
