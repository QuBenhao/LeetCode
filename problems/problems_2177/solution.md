# [Python/Go] 贪心模拟

> slug: pythongo-tan-xin-mo-ni-by-himymben-rmvl
> date: 2022-02-20
> tags: Go, Python, Python3
> question: Find Three Consecutive Integers That Sum to a Given Number (find-three-consecutive-integers-that-sum-to-a-given-number)
> url: https://leetcode.cn/problems/find-three-consecutive-integers-that-sum-to-a-given-number/solutions/EwEfbH/pythongo-tan-xin-mo-ni-by-himymben-rmvl/

---
### 解题思路
只有被三整除的数才能被拆分，且拆分方式为`num/3-1,num/3,num/3+1`

### 代码

```Python3 []
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        return [] if num % 3 else [num//3 - 1, num//3, num//3 + 1]
```
```Go []
func sumOfThree(num int64) []int64 {
    if num % 3 > 0 {
        return []int64{}
    }
    return []int64{num/3-1,num/3,num/3+1}
}
```