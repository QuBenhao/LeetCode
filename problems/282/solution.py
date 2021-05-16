import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        num, target = test_input
        return self.addOperators(num, target)

    # def addOperators(self, num, target):
    #     """
    #     :type num: str
    #     :type target: int
    #     :rtype: List[str]
    #     """
    #     self.target = target
    #     self.ans = []
    #     for i in range(1, len(num) + 1):
    #         if i > 1 and num[0] == "0":
    #             break
    #         self.dfs(num[:i], num[i:], int(num[:i]), int(num[:i]))
    #     return self.ans
    #
    # def dfs(self, curr_num, remain_num, last_val, curr_val):
    #     if not remain_num:
    #         if curr_val == self.target:
    #             if self.target == 9191:
    #                 print(last_val,curr_val)
    #             self.ans.append(curr_num)
    #         return
    #
    #     for i in range(1, len(remain_num) + 1):
    #         val = remain_num[:i]
    #         if i > 1 and remain_num[0] == "0":
    #             break
    #         self.dfs(curr_num + "+" + val, remain_num[i:], int(val), curr_val + int(val))
    #         self.dfs(curr_num + "-" + val, remain_num[i:], -int(val), curr_val - int(val))
    #         self.dfs(curr_num + "*" + val, remain_num[i:], last_val * int(val),
    #                  curr_val - last_val + last_val * int(val))

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        N, res = len(num), []

        def recur(idx, prev_operand, cur_operand, value, path):
            # Done processing all the digits in num
            if idx == N:
                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and cur_operand == 0:
                    res.append(path)
                return

            # Extending the current operand by one digit
            cur_operand = cur_operand * 10 + int(num[idx])
            str_op = str(cur_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Ex: 105. Hence this check
            if cur_operand > 0:
                # NO OP recursion
                recur(idx + 1, prev_operand, cur_operand, value, path)

            # +
            if path:
                recur(idx + 1, cur_operand, 0, value + cur_operand, path + "+" + str_op)
            else:
                recur(idx + 1, cur_operand, 0, value + cur_operand, str_op)
                # if there aren't some previous operands, we cant substract or multiply
                return
            # -
            recur(idx + 1, -cur_operand, 0, value - cur_operand, path + "-" + str_op)

            # *
            # Ex: 1 + 2 * 4
            value = value - prev_operand + (cur_operand * prev_operand)
            recur(idx + 1, cur_operand * prev_operand, 0, value, path + "*" + str_op)

        recur(0, 0, 0, 0, "")
        return res
