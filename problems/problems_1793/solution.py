import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumScore(*test_input)

    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans, curr_min, i, j, n = nums[k], nums[k], k, k, len(nums)
        while i > 0 or j < n - 1:
            # 如果右边的数大，往右推得到的最小值会更大
            if (nums[i-1] if i > 0 else 0) < (nums[j+1] if j < n-1 else 0):
                j += 1
                curr_min = min(curr_min, nums[j])
            else:
                i -= 1
                curr_min = min(curr_min, nums[i])
            ans = max(ans, curr_min * (j-i+1))
        return ans
