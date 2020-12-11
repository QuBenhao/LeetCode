import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reverseBits(test_input)

    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x = str(bin(n))[2:]
        return int(x[::-1] + "0" * (32 - len(x)), 2)