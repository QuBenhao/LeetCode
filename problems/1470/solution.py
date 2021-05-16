import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums,n = test_input
        return self.shuffle(nums,n)

    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        shuf = []
        for i in range(n):
            shuf.append(nums[i])
            shuf.append(nums[n+i])

        return shuf