# [Python] 迭代-分治思想

> Author: Benhao
> Date: 2022-02-16
> Upvotes: 13
> Tags: Python, Python3

---

### 解题思路
题目要求当且仅当，那么根节点一定和所有节点有关系对。同理，子树的根节点和所有子树的节点有关系对，而不同子树的节点间不能有关系对（会成环）。
我们从关系对最多的点开始构造树（最多必然是当前子树的根）

另外，关系对和根一样多的点，是可以和根交换的，这种时候答案要么是2要么是0。我们以此为根据，任意子树构造出现2，最终都不会是1。

### 代码

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
            
        # 没有可以作为根节点的点
        if not roots:
            return 0
        
        # 存在可以交换的根节点
        if len(roots) > 1:
            ans = 2

        # 删掉所有根节点的关系，便于统计子树的根节点
        for r in roots:
            for other in graph[r] - roots:
                graph[other] -= roots
                if not graph[other]:
                    graph.pop(other)
            graph.pop(r)
        
        # 递归
        def dfs(node):
            res = 1
            d = len(graph[node])
            # 统计和子树度数一致的关系点
            commons = {node}
            for other in graph[node]:
                if len(graph[other]) == d and len(graph[other] - graph[node]) == 1:
                    res = 2
                    commons.add(other)
                    graph.pop(other)
            # 删掉所有子树根节点
            for other in graph[node]:
                graph[other] -= commons
            # 检查是否存在不在子树里的点却和子树的节点有关系
            for block in graph.keys() - graph[node] - commons:
                if graph[block] & graph[node]:
                    return 0
            graph.pop(node)
            return res
        
        while graph:
            # 找子节点最多的节点
            node = max(graph.keys(), key=lambda x:len(graph[x]))
            ans *= dfs(node)
            if not ans:
                return 0

        return 2 if ans > 1 else ans
```