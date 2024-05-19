import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfArithmeticSlices(list(test_input))

    def numberOfArithmeticSlices(self, nums):
        """
        :type A: List[int]
        :rtype: int
        """
        # n = len(nums)
        # # 上一个差值
        # last = None
        # # 上一个差值相同的长度
        # last_len = ans = 0
        # for i in range(1, n):
        #     # 相等，差值相同长度加一
        #     if nums[i] - nums[i-1] == last:
        #         last_len += 1
        #     # 否则差值相同长度仅有刚刚这俩的差
        #     else:
        #         last_len = 1
        #     # 从头到尾一共能构成len-1种
        #     ans += last_len - 1
        #     last = nums[i] - nums[i-1]
        # return ans

        n = len(nums)
        l = r = ans = 0
        # l = n-2 剩余长度不足以再构成一个等差数列
        while l < n - 2:
            d = nums[l + 1] - nums[l]
            while r < n - 1 and nums[r + 1] - nums[r] == d:
                r += 1
            # k = r - l + 1, (k-1)*(k-2)/2 = (r-l) * (r-l-1)/2
            ans += (r-l) *(r-l-1)//2
            l = r
        return ans
