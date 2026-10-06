# [Python] Summation

> slug: python-by-himymben-f8wd
> date: 2022-04-24
> tags: Python, Python3
> question: Minimum Health to Beat Game (minimum-health-to-beat-game)
> url: https://leetcode.cn/problems/minimum-health-to-beat-game/solutions/fwyV90/python-by-himymben-f8wd/

---
### Approach
The armor can block at most the smaller of its strength and the largest attack.

### Code

```python3
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return sum(damage) + 1 - min(max(damage), armor)

```
