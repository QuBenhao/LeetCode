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
        # Find the nearest edge to x,y, which gives the number of outer rings to traverse
        x = y = n = min(xPos, yPos, num - 1 - xPos, num - 1 - yPos)
        length, cur = 0, num - 1
        # The side lengths of the outer rings form an arithmetic progression from num-1 to num-1-(n-1)*2
        length = (cur * 4 + (cur - (n - 1) * 2) * 4) * n // 2
        # Side length of the ring containing x,y
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
