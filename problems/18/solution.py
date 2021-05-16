import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, target = test_input
        return self.fourSum(nums.copy(), target)

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        N = 4
        n = len(nums)
        nums.sort()
        if n < N:
            return []
        ans = []

        def dfs(k, sum, curr_list, index):
            # implement two sum here
            if k == 2:
                left = index
                right = n - 1
                while left < right:
                    if nums[left] + nums[right] < target - sum:
                        left += 1
                    elif nums[left] + nums[right] > target - sum:
                        right -= 1
                    else:
                        l = nums[left]
                        r = nums[right]
                        c = list(curr_list)
                        c.append(l)
                        c.append(r)
                        if c not in ans:
                            ans.append(c)
                        while left < n and nums[left] == l:
                            left += 1
                        while right >= index and nums[right] == r:
                            right -= 1
                return

            for i in range(index, n + 1 - k):
                c = list(curr_list)
                c.append(nums[i])
                dfs(k - 1, sum + nums[i], c, i + 1)

        dfs(N, 0, [], 0)

        return ans
