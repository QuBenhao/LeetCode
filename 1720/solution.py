import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        encoded, first = test_input
        return self.decode(encoded, first)

    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        ans = [first] * (len(encoded)+1)
        for i in range(1,len(encoded)+1):
            ans[i] = encoded[i-1] ^ ans[i-1]
        return ans
