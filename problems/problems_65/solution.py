import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isNumber(str(test_input))

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        1:初始状态 (空字符串或者纯空格)
        2:符号位
        3:数字位 (形如-164,可以作为结束)
        4:小数点
        5:小数点后的数字(形如.721或者-123.6,可以作为结束)
        6:指数e
        7:指数后面的符号位
        8:指数后面的数字(形如+1e-6,可以作为结束)
        9:状态3,5,6后面多了空格(主要为了判断"1 1"是不合理的)
        """
        # DFA transitions: dict[action] -> successor
        states = [{},
                  # state 1
                  {"blank": 1, "sign": 2, "digit": 3, "dot": 4},
                  # state 2
                  {"digit": 3, "dot": 4},
                  # state 3
                  {"digit": 3, "dot": 5, "e|E": 6, "blank": 9},
                  # state 4
                  {"digit": 5},
                  # state 5
                  {"digit": 5, "e|E": 6, "blank": 9},
                  # state 6
                  {"sign": 7, "digit": 8},
                  # state 7
                  {"digit": 8},
                  # state 8
                  {"digit": 8, "blank": 9},
                  # state 9
                  {"blank": 9}]

        def strToAction(st):
            if '0' <= st <= '9':
                return "digit"
            if st in "+-":
                return "sign"
            if st in "eE":
                return "e|E"
            if st == '.':
                return "dot"
            if st == ' ':
                return "blank"
            return None

        currState = 1
        for c in s:
            action = strToAction(c)
            if action not in states[currState]:
                return False
            currState = states[currState][action]

        # ending states: 3,5,8,9
        return currState in {3, 5, 8, 9}

        # import re
        # # Example:              +-     1 or 1. or 1.2 or .2   e or E +- 1
        # engine = re.compile(r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?$")
        # return bool(engine.match(s.strip(" ")))  # i prefer this over putting more things (\S*) in regex

