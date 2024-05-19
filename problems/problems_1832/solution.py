import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkIfPangram(str(test_input))

    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        return len(set(sentence)) == 26
