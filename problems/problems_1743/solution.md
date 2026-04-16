# [Python] 从一个端点往另一端点遍历

> Author: Benhao
> Date: 2021-07-24
> Upvotes: 9
> Tags: Python, Python3

---

### 解题思路
固定一个方向以后，每次其实只有一种选择。

### 代码

```python3
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        connect = defaultdict(set)
        for a,b in adjacentPairs:
            connect[a].add(b)
            connect[b].add(a)
        point = min(connect.keys(), key=lambda x:(len(connect[x]), x))
        explored = {point}
        ans = [point]
        cur = point
        while len(ans) < len(connect.keys()):
            cur = (connect[cur] - explored).pop()
            explored.add(cur)
            ans.append(cur)
        return ans

```