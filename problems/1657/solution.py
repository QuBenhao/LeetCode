import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        word1, word2 = test_input
        return self.closeStrings(str(word1), str(word2))

    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        if len(word1) != len(word2):
            return False
        w1_set, w2_set = set(word1), set(word2)
        if w1_set != w2_set:
            return False
        w1_c = []
        w2_c = []

        for w in w1_set:
            w1_c.append(word1.count(w))
        for w in set(w2_set):
            w2_c.append(word2.count(w))

        return sorted(w1_c) == sorted(w2_c)

        # from collections import Counter
        # return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
