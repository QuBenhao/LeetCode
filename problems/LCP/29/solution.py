import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        num, xPos, yPos = test_input
        return self.orchestraLayout(num, xPos, yPos)

    def orchestraLayout(self, num, xPos, yPos):
        """
        :type num: int
        :type xPos: int
        :type yPos: int
        :rtype: int
        """
        # 计算离x,y最近的边，也就是遍历的外圈圈数
        x = y = n = min(xPos, yPos, num - 1 - xPos, num - 1 - yPos)
        length, cur = 0, num - 1
        # 遍历外圈长为从num-1到num-1-(n-1)*2的等差数列
        length = (cur * 4 + (cur - (n - 1) * 2) * 4) * n // 2
        # x,y所在的外圈长度
        cur -= 2 * n
        if xPos == x:
            length += yPos - y
        elif yPos == y:
            length += cur * 4 + x - xPos
        elif xPos == x + cur:
            length += cur * 3 + y - yPos
        else:
            length += cur + xPos - x
        return length % 9 + 1
