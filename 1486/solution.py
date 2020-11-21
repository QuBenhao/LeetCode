import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, start = test_input
        return self.xorOperation(n, start)

    def xorOperation(self, n, start):
        """
        O(1) solution:
        if start % 4 == 0 or 1, the second bit from right must be 0, so start ^ (start+2) == 2，
        (start + 2) ^ (start + 4) == 2 .....

        if n % 4 == 0, there will be an even number of 2, and the xor of them is 0.

        if n % 4 == 1, you can exclude the last numebr which is start + 2 * (n - 1).
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
