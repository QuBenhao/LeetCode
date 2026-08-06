# [Python] 模拟

> slug: python-mo-ni-by-himymben-ba1f
> date: 2022-03-06
> tags: Python, Python3
> question: Cells in a Range on an Excel Sheet (cells-in-a-range-on-an-excel-sheet)
> url: https://leetcode.cn/problems/cells-in-a-range-on-an-excel-sheet/solutions/BMwqgL/python-mo-ni-by-himymben-ba1f/

---
```python3
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return [chr(c) + chr(r) for c in range(ord(s[0]), ord(s[3]) + 1) for r in range(ord(s[1]), ord(s[4]) + 1)]
```