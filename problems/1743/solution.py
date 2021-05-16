import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.restoreArray([x[:] for x in test_input])

    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        import collections

        d = collections.defaultdict(list)
        start, n, appear = None, len(adjacentPairs) + 1, set()

        for a,b in adjacentPairs:
            d[a].append(b)
            d[b].append(a)

            if a in appear:
                appear.remove(a)
            else:
                appear.add(a)

            if b in appear:
                appear.remove(b)
            else:
                appear.add(b)

        ans = []
        start = list(appear)[0]
        appear = set()

        while len(ans) < n:
            ans.append(start)
            appear.add(start)
            for next in d[start]:
                if next not in appear:
                    start = next
                    break

        return ans
