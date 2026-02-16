import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reverseBits(test_input)

    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        while n:
            low_bit: int = n & -n
            length = low_bit.bit_length()
            ans |= 1 << (32 - length)
            n -= low_bit
        return ans
