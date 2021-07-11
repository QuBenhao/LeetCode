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
        # Alice 先手， 总能使得最终的和不相等
        if (a + b) % 2 == 1:
            return True
        # 两人有相同的次数，差为总能凑数9的倍数的话且足够凑出来的话，Bob胜
        if s % 9 == 0 and s // 9 == b - a >> 1:
            return False
        return True
