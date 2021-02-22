import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        s, d = test_input
        return self.findLongestWord(str(s), list(d))

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        for word in sorted(d, key = lambda w: (-len(w), w)):
            it = iter(s)
            if all(c in it for c in word): return word
        return ''

        # for word in sorted(d, key=lambda x:(-len(x), x)):
        #     i = 0
        #     for c in s:
        #         if c == word[i]:
        #             i += 1
        #         if i == len(word):
        #             return word
        # return ""
