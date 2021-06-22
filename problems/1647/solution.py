import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minDeletions(str(test_input))

    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        count = Counter(s)
        count = Counter(count.values())
        while max(count.values()) > 1:
            for k,v in count.items():
                if v > 1:
                    if k > 1:
                        count[k-1] += 1
                        count[k] -= 1
                    else:
                        count[k] -= 1
                    break
            ans += 1
        return ans
