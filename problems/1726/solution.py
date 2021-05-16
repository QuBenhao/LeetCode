import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.tupleSameProduct(list(test_input))

    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        n = len(nums)
        multiply = collections.defaultdict(list)
        for i in range(n-1):
            for j in range(i+1,n):
                multiply[nums[i]*nums[j]].append((i,j))
        ans = 0
        for k in multiply.keys():
            if len(multiply[k]) > 1:
                ans += 4 * len(multiply[k]) * (len(multiply[k]) - 1)
        return ans
