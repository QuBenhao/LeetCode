import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.interpret(test_input)

    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")
        return command
