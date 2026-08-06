# [Python] 暴力模拟

> slug: python-bao-li-mo-ni-by-himymben-yyxf
> date: 2023-03-23
> tags: C, Go, Java, Python3, TypeScript
> question: Arithmetic Subarrays (arithmetic-subarrays)
> url: https://leetcode.cn/problems/arithmetic-subarrays/solutions/Be2Kb8/python-bao-li-mo-ni-by-himymben-yyxf/

---
```Python3 []

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        return [bool((ps:=list(pairwise(sorted(nums[left: right + 1])))) and (d:=ps[0][1] - ps[0][0]) != inf and all(b - a == d for a,b in ps)) for left, right in zip(l, r)]

```
