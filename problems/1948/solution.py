import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.deleteDuplicateFolder([x[:] for x in test_input])

    def deleteDuplicateFolder(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: List[List[str]]
        """
