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
        # # 10进制 转换为 26进制，A对应1，B对应2,....Z对应26
        # while columnNumber > 0:
        #     # 最右边位为取模运算的结果
        #     columnNumber -= 1
        #     # A的ASC码 65
        #     ans.append(chr(columnNumber % 26 + 65))
        #     columnNumber //= 26
        # return ''.join(ans[::-1])

        # ans = []
        # while columnNumber > 0:
        #     curr = columnNumber % 26
        #     # 余数为1对应了A
        #     ans.append(chr(curr + 64) if curr > 0 else 'Z')
        #     # 如果发生了整除的情况，我们实际上欠了一个26
        #     columnNumber //= 26
        #     if not curr:
        #         columnNumber -= 1
        # return ''.join(ans[::-1])

        return self.convertToTitle((columnNumber - 1) // 26) + chr(
            (columnNumber - 1) % 26 + 65) if columnNumber > 0 else ''
