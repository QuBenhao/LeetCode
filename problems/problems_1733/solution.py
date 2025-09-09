from collections import Counter

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumTeachings(*test_input)

    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        languages = [set(l) for l in languages]

        dontspeak = set()
        for u, v in friendships:
            u = u-1
            v = v-1
            if languages[u] & languages[v]: continue
            dontspeak.add(u)
            dontspeak.add(v)

        langcount = Counter()
        for f in dontspeak:
            for l in languages[f]:
                langcount[l] += 1

        return 0 if not dontspeak else len(dontspeak) - max(list(langcount.values()))
