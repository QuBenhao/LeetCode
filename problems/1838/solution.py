import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxFrequency(*test_input)

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
            # 如果当前i，j不满足这个式子了，我们就移动一下最左边的指针即可，这样可以保证它和上一次的窗口大小一致
            # (如果我们遇到了最长的窗口，后面的窗口和可能始终不满足，但是答案的大小固定，我们想寻找有没有更长的窗口而已)
            if k < nums[j] * (j - i + 1):
                k -= nums[i]
                i += 1
        return j - i + 1
