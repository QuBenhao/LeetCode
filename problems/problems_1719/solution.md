# [Python] Iteration with divide and conquer

> Author: Benhao
> Date: 2022-02-16
> Upvotes: 13
> Tags: Python, Python3

---

### Approach
The statement requires an if-and-only-if relation, so the root must form a pair with every node. Likewise, each subtree root pairs with every node in that subtree. Nodes in different subtrees cannot form a pair, as this would create a cycle.
Build the tree starting with nodes having the most pairs; these must be roots of the current subtree.

A node with as many pairs as the root can swap places with it, so the answer is either 2 or 0. If any subtree has multiple constructions, the final answer cannot be 1.

### Code

```python3
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in pairs:
            graph[a].add(b)
            graph[b].add(a)
        n = len(graph)

        ans = 1
        roots = set()
        for k, v in graph.items():
            if len(v) == n - 1:
                roots.add(k)
            
        # No node can serve as the root
        if not roots:
            return 0
        
        # Interchangeable roots exist
        if len(roots) > 1:
            ans = 2

        # Remove all root relations to identify subtree roots
        for r in roots:
            for other in graph[r] - roots:
                graph[other] -= roots
                if not graph[other]:
                    graph.pop(other)
            graph.pop(r)
        
        # Recursion
        def dfs(node):
            res = 1
            d = len(graph[node])
            # Find related nodes whose degree matches the subtree
            commons = {node}
            for other in graph[node]:
                if len(graph[other]) == d and len(graph[other] - graph[node]) == 1:
                    res = 2
                    commons.add(other)
                    graph.pop(other)
            # Remove all subtree roots
            for other in graph[node]:
                graph[other] -= commons
            # Check whether a node outside the subtree is related to a node inside it
            for block in graph.keys() - graph[node] - commons:
                if graph[block] & graph[node]:
                    return 0
            graph.pop(node)
            return res
        
        while graph:
            # Find the node with the most children
            node = max(graph.keys(), key=lambda x:len(graph[x]))
            ans *= dfs(node)
            if not ans:
                return 0

        return 2 if ans > 1 else ans
```
