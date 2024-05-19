import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shuffle(*test_input)

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