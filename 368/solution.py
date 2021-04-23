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
        # # 获得有序数组
        # nums.sort()
        # # matrix[i][0]  代表 到该节点的最长步数
        # # matrix[i][1] 代表 最长步数时的上一个节点
        # matrix = [(0,0)] * n
        #
        # maxDis = maxPos = -1
        # # 从前往后遍历
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[j]%nums[i]==0:
        #             # 满足题目条件的情况下
        #             # 若从当前节点（i）往目标节点（j）的步数较之前的元素更大，则更新最长步数与上一个节点
        #             if matrix[i][0]+1 > matrix[j][0]:
        #                 matrix[j] = (matrix[i][0] + 1, i)
        #
        #     # 每一轮遍历结束后检查是否为最大值（当前节点i的最大步数只由i之前的元素决定）
        #     # 记录下最大值所在的位置
        #     if matrix[i][0]>maxDis:
        #         maxDis = matrix[i][0]
        #         maxPos = i
        #
        # # 根据最大步数所在的位置，逆向推出所选子集
        # re = []
        # re.append(nums[maxPos])
        # while matrix[maxPos][0]!=0:
        #     re.append(nums[matrix[maxPos][1]])
        #     maxPos = matrix[maxPos][1]
        # re.reverse()
        # return re
