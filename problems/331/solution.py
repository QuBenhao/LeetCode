import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isValidSerialization(str(test_input))

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(",")
        total = 1

        # for node in nodes:
        #     if total == 0:
        #         return False
        #     if node != '#':
        #         total += 1
        #     else:
        #         total -= 1

        for node in nodes:
            total -= 1
            if total < 0:
                return False
            if node != '#':
                total += 2

        return total == 0
