import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numIdenticalPairs(test_input)

    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        appear_time = {}
        sum = 0
        for i in nums:
            if i in appear_time:
                sum += appear_time[i]
                appear_time[i] += 1
            else:
                appear_time[i] = 1
        return sum
