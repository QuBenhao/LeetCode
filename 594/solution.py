import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findLHS(list(test_input))

    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter()
        for num in nums:
            c[num] += 1
        ans = 0
        for k in c.keys():
            if k + 1 in c:
                ans = max(ans, c[k] + c[k+1])
        return ans
