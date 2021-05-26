import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        sequence, word = test_input
        return self.maxRepeating(str(sequence), str(word))

    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        # ans, match = 0, word
        # while sequence.find(match) != -1:
        #     ans += 1
        #     match += word
        # return ans

        m, n = len(sequence), len(word)
        dp = [0] * m
        for i, c in enumerate(sequence):
            if c == word[0] and sequence[i:i + n] == word:
                dp[i + n - 1] = max(dp[i - 1] + 1, dp[i + n - 1])
        return max(dp)
