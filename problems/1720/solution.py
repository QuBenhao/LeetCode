import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.decode(*test_input)

    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        last = first
        for i in range(len(encoded)):
            encoded[i] ^= last
            last = encoded[i]
        return [first] + encoded
