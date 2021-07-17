import solution
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.groupAnagrams([str(x) for x in test_input])

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def hashCounter(s):
            cnts = [0] * 26
            for c in s:
                cnts[ord(c) - ord('a')] += 1
            return tuple(cnts)

        ans = defaultdict(list)
        for s in strs:
            ans[hashCounter(s)].append(s)
        return [v for v in ans.values()]

        # ans = defaultdict(list)
        # for s in strs:
        #     ans[''.join(sorted(s))].append(s)
        # return list(ans.values())
