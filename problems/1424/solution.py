import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findDiagonalOrder(test_input)

    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums:
            return []

        res = []

        for i, l in enumerate(nums):
            for j, val in enumerate(nums[i]):
                if len(res) <= i + j:
                    res.append([val])
                else:
                    res[i+j].insert(0,val)
        ans = []
        for l in res:
            ans.extend(l)
        return ans
