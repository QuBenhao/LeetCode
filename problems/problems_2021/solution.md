# [Python] 差分数组

> slug: python-cha-fen-shu-zu-by-himymben-2kx5
> date: 2022-05-04
> tags: Python, Python3
> question: Brightest Position on Street (brightest-position-on-street)
> url: https://leetcode.cn/problems/brightest-position-on-street/solutions/5HoyEG/python-cha-fen-shu-zu-by-himymben-2kx5/

---
### 解题思路

模板题，不过需要扁平化差分的距离

### 代码

```python3
class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        diff = defaultdict(int)
        for p, r in lights:
            diff[p - r] += 1
            diff[p + r + 1] -= 1
        d, mx, ans = 0, 0, None
        for k in sorted(diff.keys()):
            d += diff[k]
            if d > mx:
                mx, ans = d, k
        return ans

```
