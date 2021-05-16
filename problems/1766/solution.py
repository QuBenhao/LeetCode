import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, edges = test_input
        return self.getCoprimes(list(nums), [x[:] for x in edges])

    def getCoprimes(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        try:
            from math import gcd
        except:
            from fractions import gcd
        from collections import defaultdict

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        ans = [-1] * len(nums)
        path = defaultdict(list)

        def dfs(node, depth, parent):
            largest_depth = -1
            for val in path:
                if gcd(nums[node], val) == 1:
                    if path[val] and path[val][-1][1] > largest_depth:
                        ans[node] = path[val][-1][0]
                        largest_depth = path[val][-1][1]
            path[nums[node]].append((node, depth))
            for node_ in graph[node]:
                if node_ != parent:
                    dfs(node_, depth + 1, node)
            path[nums[node]].pop()

        dfs(0, 0, -1)
        return ans
