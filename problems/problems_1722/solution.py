import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumHammingDistance(*test_input)

    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        import collections

        def diff(so, ta):
            count = 0
            for i in range(len(so)):
                if so[i] != ta[i]:
                    count += 1
            return count

        def helper(indexes, so, ta):
            s_d = collections.defaultdict(int)
            t_d = collections.defaultdict(int)
            for i in set(indexes):
                s_d[so[i]] += 1
                t_d[ta[i]] += 1
            count = 0
            for k in t_d:
                if k not in s_d:
                    count += t_d[k]
                else:
                    count += max(t_d[k] - s_d[k], 0)
            # print(t_d,s_d,count)
            return count

        states = set()
        actions = collections.defaultdict(set)
        for a, b in allowedSwaps:
            states.add(a)
            states.add(b)
            actions[a].add(b)
            actions[b].add(a)

        group = []
        explored = set()
        curr = list(states)
        while curr:
            s = curr.pop(0)
            frontier = [s]
            res = set()
            while frontier:
                n_ = []
                for s in frontier:
                    explored.add(s)
                    res.add(s)
                    for n in actions[s]:
                        if n not in explored:
                            n_.append(n)
                frontier = n_
            for r in res:
                if r in curr:
                    curr.remove(r)
            group.append(res)
        # print(group)
        if not group:
            return diff(source, target)
        else:
            ans = 0
            for g in group:
                ans += helper(g, source, target)
            for i in range(len(source)):
                if i not in explored:
                    if source[i] != target[i]:
                        ans += 1
            return ans
