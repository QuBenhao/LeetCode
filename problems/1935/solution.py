import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canBeTypedWords(str(test_input[0]), str(test_input[1]))

    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        bk = set(brokenLetters)
        return sum(all(c not in bk for c in s) for s in text.split(' '))
