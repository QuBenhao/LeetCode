# [Python] BFS

> slug: python-bfs-by-himymben-cwxb
> date: 2024-03-09
> tags: C, Go, Java, Python3, TypeScript
> question: Minimum Genetic Mutation (minimum-genetic-mutation)
> url: https://leetcode.cn/problems/minimum-genetic-mutation/solutions/b4tDA9/python-bfs-by-himymben-cwxb/

---

> Problem: [433. 最小基因变化](https://leetcode.cn/problems/minimum-genetic-mutation/description/)

[TOC]

# 思路

> 从bank中得到可以进行的转换

# 解题方法

> 从头到尾看看能否BFS


# Code
```Python3 []
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def dist(a, b):
            return sum(1 if ca != cb else 0 for ca, cb in zip(a, b))

        if endGene not in bank:
            return -1
        trans = defaultdict(list)
        for a, b in combinations(bank + [startGene], 2):
            if dist(a, b) == 1:
                trans[a].append(b)
                trans[b].append(a)
        queue, explored, step = deque([startGene]), {startGene}, 0
        while queue:
            length = len(queue)
            for _ in range(length):
                cur = queue.popleft()
                if cur == endGene:
                    return step
                for nxt in trans[cur]:
                    if nxt not in explored:
                        explored.add(nxt)
                        queue.append(nxt)
            step += 1
        return -1
```
  
