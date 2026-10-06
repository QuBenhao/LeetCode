import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.convertToTitle(test_input)

    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        # ans = []
        # # Convert base 10 to base 26: A represents 1, B represents 2, ... Z represents 26
        # while columnNumber > 0:
        #     # The rightmost digit is the result of the modulo operation
        #     columnNumber -= 1
        #     # A has ASCII code 65
        #     ans.append(chr(columnNumber % 26 + 65))
        #     columnNumber //= 26
        # return ''.join(ans[::-1])

        # ans = []
        # while columnNumber > 0:
        #     curr = columnNumber % 26
        #     # A remainder of 1 corresponds to A
        #     ans.append(chr(curr + 64) if curr > 0 else 'Z')
        #     # If the division is exact, we still owe a value of 26
        #     columnNumber //= 26
        #     if not curr:
        #         columnNumber -= 1
        # return ''.join(ans[::-1])

        return self.convertToTitle((columnNumber - 1) // 26) + chr(
            (columnNumber - 1) % 26 + 65) if columnNumber > 0 else ''
