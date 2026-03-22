import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findRotation(*test_input)

    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        for _ in range(4):
            if mat == target:
                return True
            mat = [list(row) for row in zip(*mat[::-1])]
        return False
