import solution
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestDivisibleSubset(list(test_input))

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        dp = defaultdict(list)
        ans = []
        for num in nums:
            max_list = []
            for key, val in dp.items():
                if num % key == 0 and len(val) > len(max_list):
                    max_list = val
            if not max_list:
                dp[num] = [num]
            else:
                dp[num] = max_list + [num]
            if len(dp[num]) > len(ans):
                ans = dp[num]
        return ans

        # nums.sort()
        # n = len(nums)
        # dp = [[num] for num in nums]
        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
        #             dp[i] = dp[j] + [nums[i]]
        # return max(dp,key=len)

        # n = len(nums)
        # # Obtain a sorted array
        # nums.sort()
        # # matrix[i][0] is the maximum number of steps to this node
        # # matrix[i][1] is the predecessor on the longest path
        # matrix = [(0,0)] * n
        #
        # maxDis = maxPos = -1
        # # Traverse from beginning to end
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[j]%nums[i]==0:
        #             # If the problem's condition is satisfied
        #             # If the path from current node i to target node j is longer than the previous best, update the length and predecessor
        #             if matrix[i][0]+1 > matrix[j][0]:
        #                 matrix[j] = (matrix[i][0] + 1, i)
        #
        #     # After each iteration, check for a new maximum (the best length at node i depends only on preceding elements)
        #     # Record the index of the maximum
        #     if matrix[i][0]>maxDis:
        #         maxDis = matrix[i][0]
        #         maxPos = i
        #
        # # Reconstruct the selected subset backward from the index with the maximum path length
        # re = []
        # re.append(nums[maxPos])
        # while matrix[maxPos][0]!=0:
        #     re.append(nums[matrix[maxPos][1]])
        #     maxPos = matrix[maxPos][1]
        # re.reverse()
        # return re
