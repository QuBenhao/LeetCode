import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, k = test_input
        return self.maxFrequency(list(nums), k)

    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = j = 0
        # 排序后从小到大，这样判断k能否使i,j间的nums全部到nums[j]
        nums.sort()
        for j in range(len(nums)):
            # k多了nums[j]步
            k += nums[j]
            # nums[j] * (j - i + 1) 代表 从全部为0到全部为nums[j]所需的步数
            # 如果k比全部变为nums[j]所需的步数小，需要抛去最左边的值（因为最左边的距离当前的最远）
            # 考虑上一个j: j-1的时候，k >= nums[j-1] * (j - i) 所以i才能是j时的i
            # nums[j-1] * (j-i) + nums[j] <= k + nums[j] < nums[j] * (j - i + 1)
            # 相当于k置于nums[j-1] * (j-i)到nums[j] * (j-i)之间, 且此时j-i+1保持不变
            if k < nums[j] * (j - i + 1):
                k -= nums[i]
                i += 1
        return j - i + 1
