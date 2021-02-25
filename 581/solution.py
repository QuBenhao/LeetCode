import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findUnsortedSubarray(list(test_input))

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m, m_index, start, end = float("-inf"), -1, len(nums), -1
        for i, n in enumerate(nums):
            if n > m:
                m = n
                m_index = i
            elif n < m:
                start = min(m_index, start)
                end = max(i, end)
        m, m_index = float("inf"), -1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < m:
                m = nums[i]
                m_index = i
            elif nums[i] > m:
                start = min(i, start)
                end = max(m_index, end)
        if start == len(nums) or end == -1:
            return 0
        return end - start + 1
