# [Python] 排序+二分

> Author: Benhao
> Date: 2023-11-10
> Upvotes: 1
> Tags: Binary Search, Sorting, Python3

---

> Problem: [2300. 咒语和药水的成功对数](https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/description/)


# Code
```Python3 []
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        return [len(sp) - bisect_left(sp, success / s) for s in spells] if (sp := sorted(potions)) else []
```
  