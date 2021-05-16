import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.calculate(str(test_input))

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign, last = 0, 0, 1, 0
        for c in s + '+':
            if "0" <= c <= "9":
                num = num * 10 + int(c)
            elif c != ' ':
                if sign == 2:
                    last *= num
                elif sign == 3:
                    last = last // num if last >= 0 else - (-last // num)
                else:
                    last = num * sign
                if c == '+' or c == '-':
                    res += last
                    sign = 1 if c == "+" else -1
                    last = 0
                else:
                    sign = 2 if c == "*" else 3
                num = 0
        return res
