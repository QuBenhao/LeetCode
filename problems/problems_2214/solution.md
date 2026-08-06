# [Python] 求和

> slug: python-by-himymben-f8wd
> date: 2022-04-24
> tags: Python, Python3
> question: Minimum Health to Beat Game (minimum-health-to-beat-game)
> url: https://leetcode.cn/problems/minimum-health-to-beat-game/solutions/fwyV90/python-by-himymben-f8wd/

---
### 解题思路
护甲最多抵挡最大那次攻击里，两者的最小值

### 代码

```python3
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return sum(damage) + 1 - min(max(damage), armor)

```