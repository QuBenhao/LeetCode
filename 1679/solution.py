import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, k = test_input
        return self.maxOperations(nums,k)

    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        counter = dict()
        ans = 0
        for num in nums:
            if k - num in counter:
                if counter[k-num] == 1:
                    del counter[k-num]
                else:
                    counter[k-num] -= 1
                ans += 1
            elif num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        return ans

        # nums.sort()
        # i, j = 0, len(nums) - 1
        # res = 0
        # while i < j:
        #     summ = nums[i] + nums[j]
        #     if summ == k:
        #         i += 1
        #         j -= 1
        #         res += 1
        #     elif summ < k:
        #         i += 1
        #     else:
        #         j -= 1
        # return res
