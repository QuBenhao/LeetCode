import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.deleteAndEarn(list(test_input))

    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        ns = sorted(cnt.keys())
        # Dynamic programming for the current maximum and the maximum before the previous value
        max_so_far = cnt[ns[0]] * ns[0]
        max_except_last = 0
        for i in range(1,len(cnt)):
            if ns[i-1] == ns[i] - 1:
                max_except_last, max_so_far = max_so_far, max(max_so_far, max_except_last + cnt[ns[i]] * ns[i])
            else:
                max_except_last,max_so_far = max_so_far, max_so_far + cnt[ns[i]] * ns[i]
        return max_so_far
