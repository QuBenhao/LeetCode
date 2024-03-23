import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mergeAlternately(*test_input)

    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = []
        i1, i2, n1, n2 = 0, 0, len(word1), len(word2)
        while i1 < n1 and i2 < n2:
            ans.append(word1[i1])
            ans.append(word2[i2])
            i1 += 1
            i2 += 1
        if i1 < n1:
            ans.append(word1[i1:])
        elif i2 < n2:
            ans.append(word2[i2:])
        return "".join(ans)
