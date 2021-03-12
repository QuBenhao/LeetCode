import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        guess, answer = test_input
        return self.game(list(guess), list(answer))

    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        return sum(guess[i] == answer[i] for i in range(len(guess)))
