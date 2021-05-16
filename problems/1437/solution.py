import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, k = test_input
        return self.kLengthApart(list(nums), k)

    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        count = k
        for num in nums:
            if num:
                if count < k:
                    return False
                count = 0
            else:
                count += 1
        return True

        # last = -k - 1
        # for i,num in enumerate(nums):
        #     if num:
        #         if last >= i - k:
        #             return False
        #         last = i
        # return True
