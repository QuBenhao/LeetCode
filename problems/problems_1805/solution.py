import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numDifferentIntegers(str(test_input))

    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        import re
        return len(set(map(int, re.sub('[^0-9]', ' ', word).split())))

        # ans = set()
        # last = None
        # for c in word + "#":
        #     if '0' <= c <= '9':
        #         if last is None:
        #             last = int(c)
        #         else:
        #             last *= 10
        #             last += int(c)
        #     elif last is not None:
        #         ans.add(last)
        #         last = None
        # return len(ans)
