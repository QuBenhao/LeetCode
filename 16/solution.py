import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, target = test_input
        return self.threeSumClosest(nums.copy(), target)

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def dfs(k, curr_sum, index, result):
            # implement two sum here
            if k == 2:
                left = index
                right = n - 1
                while left < right:
                    if abs(nums[left] + nums[right] + curr_sum - target) < abs(target - result):
                        result = nums[left] + nums[right] + curr_sum
                    if nums[left] + nums[right] < target - curr_sum:
                        left += 1
                    elif nums[left] + nums[right] > target - curr_sum:
                        right -= 1
                    else:
                        return target
                return result

            for i in range(index, n + 1 - k):
                result = dfs(k - 1, curr_sum + nums[i], i + 1, result)
                if result == target:
                    return target
            return result

        N = 3
        n = len(nums)
        nums.sort()

        return dfs(N, 0, 0, float("inf"))
