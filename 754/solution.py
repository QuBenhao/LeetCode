import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reachNumber(test_input)

    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        import math
        target = abs(target)
        # about = int((math.sqrt(1+8*target)-1)/2) + 1
        about = int(math.sqrt(2*target))
        while about * (about + 1) // 2 > target:
            about -= 1
        if target == about * (about + 1) // 2:
            return about
        about += 1
        while (about + 1) * about // 2 % 2 != target % 2:
            about += 1
        return about
