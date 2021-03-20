import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.evalRPN(list(test_input))

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if c == '+':
                    stack.append(num1 + num2)
                elif c == '-':
                    stack.append(num1 - num2)
                elif c == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(float(num1) / num2))
        return stack[0]

        # from operator import add, sub, mul
        # op_to_binary_fn = {
        #     "+": add,
        #     "-": sub,
        #     "*": mul,
        #     "/": lambda x, y: int(float(x) / y),  # 需要注意 python 中负数除法的表现与题目不一致
        # }
        #
        # stack = list()
        # for token in tokens:
        #     try:
        #         num = int(token)
        #     except ValueError:
        #         num2 = stack.pop()
        #         num1 = stack.pop()
        #         num = op_to_binary_fn[token](num1, num2)
        #     finally:
        #         stack.append(num)
        #
        # return stack[0]
