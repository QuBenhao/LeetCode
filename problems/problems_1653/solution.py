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
        #     # 到i有多少个'b'，后面有多少个'a'
        #     b = i - count[i]
        #     a = count[-1] - count[i+1]
        #     if not a and not b:
        #         return 0
        #     ans = min(ans, b+a)
        # return ans

        # b的个数
        cnt = ans = 0
        for c in s:
            if c == 'b':
                # 'b'为结尾，必然不影响之前的平衡性
                cnt += 1
            else:
                # 'a'为结尾，要么是上一个的平衡结果再删掉这个'a',要么要删光前面的'b'
                ans = min(ans + 1, cnt)
        return ans
