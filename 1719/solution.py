import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkWays([x[:] for x in test_input])

    def checkWays(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        import collections

        """
        we can iterate each node and check their validity by their degree. 
        As node with larger degree more tends to be an ancestor.

        For each node x, we find out its parent p. p is the node that has been visited (in the set ancestor) 
        and has the lowest degree in g[x] (connected with x in pairs). 
        Then g[x] must be a subset of g[p] | {p} since x's ancestors are p + p's ancestors 
        and x +x's descendants are all p's descendants.
        If x has no parent, it's the root whose degree should be n-1.
        
        We only need to check p for x as if all p-x relations are solid, the entire tree is well founded.
        
        Another reason we check p is that p could be exchanged with x. If it is (len(g[p]) == len(g[x]) and remember, 
        we have checked g[x].issubset(g[p]|{p})), we have more than one way to contruct the tree.
        """

        g = collections.defaultdict(set)
        for x, y in pairs:
            g[x].add(y)
            g[y].add(x)
        n, mul = len(g), False
        ancestor = set()
        for x in sorted(g.keys(), key=lambda i: -len(g[i])):
            p = min((g[x] & ancestor), key=lambda i: len(g[i]), default=0)  # find x's parent p
            ancestor.add(x)
            if p:
                if not g[x].issubset(g[p] | {p}):
                    return 0
                mul |= len(g[p]) == len(g[x])
            elif len(g[x]) != n - 1:
                return 0
        return 1 + mul

        # adj = collections.defaultdict(set)
        # for x, y in pairs:
        #     adj[x].add(y)
        #     adj[y].add(x)
        # n, mul = len(adj), False
        # lookup = set()
        # for node in sorted(adj.keys(), key=lambda i: len(adj[i]), reverse=True):
        #     lookup.add(node)
        #     parent = 0
        #     for x in adj[node]:
        #         if x not in lookup:
        #             continue
        #         if parent == 0 or len(adj[x]) < len(adj[parent]):
        #             parent = x
        #     if parent:
        #         if any(True for x in adj[node] if x != parent and x not in adj[parent]):
        #             return 0
        #         mul |= len(adj[parent]) == len(adj[node])
        #     elif len(adj[node]) != n-1:
        #         return 0
        # return 1 + mul
