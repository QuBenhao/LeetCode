import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSwaps(str(test_input))

    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = count = 0
        for c in s:
            if c == '[':
                count += 1
            else:
                if not count:
                    # Swap this ']' with the rightmost '['; later count increases by 1, but equal total counts keep later closing brackets valid
                    ans += 1
                    count += 1
                else:
                    count -= 1
        return ans
