import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        sentence1, sentence2 = test_input
        return self.areSentencesSimilar(str(sentence1), str(sentence2))

    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        if len(sentence1) > len(sentence2):
            s1,s2 = s2,s1
        l = set([i for i in range(len(s2))])
        i = -1
        for s in s1:
            try:
                i = s2.index(s, i+1)
                l.remove(i)
            except:
                return False
        return not l or sum(l) == (min(l) + (len(l) + min(l) - 1)) * len(l) // 2
