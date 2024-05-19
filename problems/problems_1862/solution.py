import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumOfFlooredPairs(list(test_input))

    def sumOfFlooredPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10 ** 9 + 7

        upper = max(nums)
        cnt = [0] * (upper + 1)
        for num in nums:
            cnt[num] += 1

        presum = [0] * (upper + 1)
        for i in range(1, upper + 1):
            presum[i] = presum[i - 1] + cnt[i]

        ans = 0
        for y in range(1, upper + 1):
            if cnt[y]:
                d = 1
                while d * y <= upper:
                    # 所有在 (d + 1) * y - 1 到 d * y的数 x，都满足 x // y = d
                    ans += cnt[y] * d * (presum[min((d + 1) * y - 1, upper)] - presum[d * y - 1])
                    d += 1
        return ans % mod
