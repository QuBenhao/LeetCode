import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.subsetXORSum(list(test_input))

    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        total = [0]
        for num in nums:
            new = []
            for i in total:
                ans += i ^ num
                new.append(i ^ num)
            total += new
        return ans
