# [Python] Bitmask enumeration

> slug: python-er-jin-zhi-mei-ju-by-himymben-zoiy
> date: 2022-09-03
> tags: Python, Python3
> question: Maximum Rows Covered by Columns (maximum-rows-covered-by-columns)
> url: https://leetcode.cn/problems/maximum-rows-covered-by-columns/solutions/gzs0DX/python-er-jin-zhi-mei-ju-by-himymben-zoiy/

---
### Approach
Encode every row using the same bitmask convention.
After enumerating a set of columns, quickly check whether they cover each row.

### Code

```python3
class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        def to_num(row):
            res = 0
            for num in row:
                res <<= 1
                res += num
            return res

        ans = 0
        nums = [to_num(r) for r in mat]
        for comb in combinations(range(len(mat[0])), cols):
            num = sum(1 << i for i in comb)
            ans = max(ans, sum((num & n) == n for n in nums))
        return ans
```
