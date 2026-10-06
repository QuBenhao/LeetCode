import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumGame(str(test_input))

    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        s = a = b = 0
        n = len(num)
        for i,c in enumerate(num):
            if i < n // 2:
                if c == '?':
                    a += 1
                else:
                    s += int(c)
            else:
                if c == '?':
                    b += 1
                else:
                    s -= int(c)
        # Alice moves first and can ensure the final sums differ
        if (a + b) % 2 == 1:
            return True
        # With equal move counts, Bob wins if the difference is a multiple of 9 that the remaining pairs can make up
        if s % 9 == 0 and s // 9 == b - a >> 1:
            return False
        return True
