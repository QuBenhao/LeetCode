# [Python] 按怪物到达时间分类

> Author: Benhao
> Date: 2021-07-04
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
优先消灭这些先到达的怪物，如果怎么也不够消灭了，就返回。
注意分类时，按天花板除-1，也就是每个点都是(k-1，k]。
这是因为第k分钟时，所有这个区间内的都能到达了。

### 代码

```python3
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        cnts = Counter()
        for d,s in zip(dist,speed):
            cnts[ceil(d/s)-1] += 1
        ans = 0
        for k in sorted(cnts.keys()):
            if cnts[k] > k + 1 - ans:
                return k + 1
            ans += cnts[k]
        return ans
```