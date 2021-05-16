import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfSteps(test_input)

    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        # using binary is better than for loop
        # 14 = 1110, step = 3 + 4 - 1 = 6
        # 8 = 1000, step = 1 + 4 - 1 = 4
        # This is because divide an even number by 2 will cause 1 -> 0 in binary, and our goal is all 0
        """
        We have to erase each bit by the following rules:
            0 -> erase
            1 -> 0 -> erase
            But the first 1 bit will only need to 1 -> 0.
        """
        # 1000 -> 100 -> 10 -> 1 -> 0
        digits = bin(num)[2:]
        return digits.count('1') - 1 + len(digits)
