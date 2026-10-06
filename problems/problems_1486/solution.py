import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.xorOperation(*test_input)

    def xorOperation(self, n, start):
        """
        O(1) solution:
        if start % 4 == 0 or 1, the second bit from right must be 0, so start ^ (start+2) == 2，
        (start + 2) ^ (start + 4) == 2 .....

        if n % 4 == 0, there will be an even number of 2, and the xor of them is 0.

        if n % 4 == 1, you can exclude the last number which is start + 2 * (n - 1).
        The xor of left numbers is 0, so the result is last.

        if n % 4 == 2, you can exclude the last two numbers. The xor of left numbers is 0,
        so the result is the xor of last two numbers which is 2.
        
        if n % 4 == 3, you can exclude the last three numbers. The xor of left numbers is 0,
        so the result is the xor of last three numbers which is 2 ^ last.

        if start % 4 == 2 or 3, the second bit from right is 1, but the (start + 2) % 4 == 0 or 1.
        So we can exclude the first number.
        So the solution to calculate the left numbers is the same as the solution above.
        """
        last = start + 2 * (n - 1)
        if start % 4 < 2:
            start = 0
        else:
            n -= 1
        if n % 2 == 0: return start ^ (n & 2)
        return start ^ last ^ (n & 2)

        # def cal(x):
        #     """
        #         4a ^ (4a + 1) = 1
        #         4a ^ (4a + 1) ^ (4a + 2) = 1 ^ (4a + 2) = 4a + 3
        #         4a ^ (4a + 1) ^ (4a + 2) ^ (4a + 3) = (4a + 3) ^ (4a + 3) = 0
        #     """
        #     if x % 4 == 0:
        #         return x
        #     elif x % 4 == 1:
        #         return 1
        #     elif x % 4 == 2:
        #         return x + 1
        #     return 0
        #
        # # Divide everything by 2 and use the %4 rule to calculate all but the least significant bit of ans
        # s = start >> 1
        # # XOR 1 through s - 1 and 1 through s + n - 1; XORing these results gives all but the last bit of ans
        # prefix = cal(s - 1) ^ cal(s + n - 1)
        # # Use parity to calculate the least significant bit of ans
        # last = n & start & 1
        # return prefix << 1 | last
