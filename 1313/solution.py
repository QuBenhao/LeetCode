import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.decompressRLElist(test_input)

    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(int(len(nums)/2)):
            for j in range(nums[2*i]):
                output.append(nums[2*i+1])
        return output
