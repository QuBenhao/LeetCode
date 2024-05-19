import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minMoves(*test_input)

    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        # 最终的两数之和只能在[2, 2 * limit]之间
        diff = [0] * (2 * limit + 2)
        # 对于每个nums[i],nums[n-1-i]来说：
        # 不需要修改的只有 diff[a + b]
        # 只需要修改一次的为 [1 + min(a, b), limit + max(a, b) + 1)
        # 剩下的部分需要修改两次
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            # 需要修改两次
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            # 需要修改一次
            diff[1 + min(a, b)] -= 1
            diff[limit + max(a, b) + 1] += 1
            # 需要修改零次
            diff[a + b] -= 1
            diff[a + b + 1] += 1
        res, s = n, 0
        for i in range(2, 2 * limit + 1):
            s += diff[i]
            res = min(res, s)
        return res
