import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxCoins(test_input)

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # add nums[-1] = 1 and nums[n] = 1
        nums = [1] + nums + [1]
        n = len(nums) - 1
        m = [[0 for i in range(n)] for j in range(n)]

        # l: the length of chain
        for l in range(1,n):
            # i: left index
            for i in range(n-l):
                j = i+l
                # slice i,j chain with index k
                m[i][j] = max(m[i][k] + m[k+1][j] + nums[i-1]*nums[k]*nums[j] for k in range(i,j))

        return m[0][n-1]
