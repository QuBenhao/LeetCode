import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSumMinProduct(list(test_input))

    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10 ** 9 + 7
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(n):
            # sum(i,j) = presum[j+1] - presum[i]
            presum[i+1] = presum[i] + nums[i]

        # 双向单调栈
        # 左边第一个比i小的下标
        left = [-1] * n
        # 右边第一个比i小的下标
        right = [n] * n

        # 单调栈
        stack = []
        for i in range(n):
            # 单调递增栈
            while stack and nums[i] < nums[stack[-1]]:
                # 当前元素比栈中最后一个元素小，那么栈中最后一个元素右边第一个比它小的就是当前元素了
                right[stack.pop()] = i
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            # 单调递增栈
            while stack and nums[i] < nums[stack[-1]]:
                # 当前元素比栈中最后一个元素小，那么栈中最后一个元素左边第一个比它小的就是当前元素了
                left[stack.pop()] = i
            stack.append(i)

        res = 0
        for i in range(n):
            res = max(res, nums[i] * (presum[right[i]] - presum[left[i]+1]))
        return res % mod
