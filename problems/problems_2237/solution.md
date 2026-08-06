# [Python] 差分数组

> slug: python-chai-fen-shu-zu-by-himymben-6vnw
> date: 2022-04-24
> tags: Python, Python3
> question: Count Positions on Street With Required Brightness (count-positions-on-street-with-required-brightness)
> url: https://leetcode.cn/problems/count-positions-on-street-with-required-brightness/solutions/z3uACX/python-chai-fen-shu-zu-by-himymben-6vnw/

---
### 解题思路
差分数组应用题

### 代码

```python3
class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        diff = [0] * (n + 1)
        for p, r in lights:
            diff[max(0, p - r)] += 1
            diff[min(n, p + r + 1)] -= 1
        ans = cur = 0
        for r, d in zip(requirement, diff):
            cur += d
            ans += int(cur >= r)
        return ans

```