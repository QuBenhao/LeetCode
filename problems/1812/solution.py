import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.squareIsWhite(str(test_input))

    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        return (ord(coordinates[0]) - 97 + ord(coordinates[1]) - 49) % 2 == 1
