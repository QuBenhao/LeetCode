import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumSize(*test_input)

    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """

        def helper(target):
            if target == 0:
                return maxOperations + 1
            count = 0
            for num in nums:
                count += (num - 1) // target
            return count <= maxOperations

        n = len(nums)
        s = sum(nums)
        left, right = max(s // (n + maxOperations), 1), max(nums)
        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return left
