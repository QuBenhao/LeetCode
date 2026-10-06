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

        # Monotonic stacks in both directions
        # Index of the first smaller element left of i
        left = [-1] * n
        # Index of the first smaller element right of i
        right = [n] * n

        # Monotonic stack
        stack = []
        for i in range(n):
            # Monotonically increasing stack
            while stack and nums[i] < nums[stack[-1]]:
                # If the current element is smaller than the stack top, it is that element's first smaller element to the right
                right[stack.pop()] = i
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            # Monotonically increasing stack
            while stack and nums[i] < nums[stack[-1]]:
                # If the current element is smaller than the stack top, it is that element's first smaller element to the left
                left[stack.pop()] = i
            stack.append(i)

        res = 0
        for i in range(n):
            res = max(res, nums[i] * (presum[right[i]] - presum[left[i]+1]))
        return res % mod
