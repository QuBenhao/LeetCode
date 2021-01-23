import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.decode(list(test_input))

    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        start = 0
        for i in range(1, len(encoded) + 2):
            start ^= i
        curr = 0
        for encode in encoded:
            curr ^= encode
            start ^= curr
        result = [start]
        for encode in encoded:
            result.append(encode ^ result[-1])
        return result
