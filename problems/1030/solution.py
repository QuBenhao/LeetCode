import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        R, C, r0, c0 = test_input
        return self.allCellsDistOrder(R, C, r0, c0)

    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """

        return sorted([[r, c] for r in range(R) for c in range(C)], key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))

        # cells = []
        # for r in range(R):
        #     for c in range(C):
        #         cells.append([r, c])
        # cells.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        # return cells
