import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countConsistentStrings(*test_input)

    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed = [char for char in allowed]
        count = 0
        for word in words:
            allow = True
            for c in word:
                if c not in allowed:
                    allow = False
                    break
            if allow:
                count += 1
        return count
