import solution
import math


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSwaps(str(test_input))

    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = s.count('1')
        if res != len(s) // 2 and res != math.ceil(len(s)/2):
            return -1
        if len(s) % 2 == 0:
            ans1 = ans2 = 0
            for i,c in enumerate(s):
                if i % 2:
                    if c == '1':
                        ans2 += 1
                else:
                    if c == '1':
                        ans1 += 1
            return min(ans1, ans2)
        elif res == len(s) // 2:
            ans = 0
            for i,c in enumerate(s):
                if i % 2 == 0 and c == '1':
                    ans += 1
            return ans
        else:
            ans = 0
            for i,c in enumerate(s):
                if i % 2 == 0 and c == '0':
                    ans += 1
            return ans
