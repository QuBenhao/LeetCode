import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumDeletions(str(test_input))

    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # n = len(s)
        # count = [0] * (n + 1)
        # for i,c in enumerate(s):
        #     if c == 'a':
        #         count[i+1] = count[i] + 1
        #     else:
        #         count[i+1] = count[i]
        # ans = float("inf")
        # for i in range(n):
        #     # Count 'b' characters through i and 'a' characters after i
        #     b = i - count[i]
        #     a = count[-1] - count[i+1]
        #     if not a and not b:
        #         return 0
        #     ans = min(ans, b+a)
        # return ans

        # Number of b characters
        cnt = ans = 0
        for c in s:
            if c == 'b':
                # Ending with 'b' preserves the previous balance
                cnt += 1
            else:
                # For a final 'a', either delete it after balancing the prefix or delete all preceding 'b' characters
                ans = min(ans + 1, cnt)
        return ans
