import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getXORSum(*test_input)

    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # (a1^a2) & (b1^b2) = (a1&b1) ^ (a1&b2) ^ (a2&b1) ^ (a2&b2)
        n1, n2 = len(arr1), len(arr2)
        ans = 0
        for i in range(n1):
            ans ^= arr1[i]
        ans1 = 0
        for j in range(n2):
            ans1 ^= arr2[j]
        return ans & ans1
