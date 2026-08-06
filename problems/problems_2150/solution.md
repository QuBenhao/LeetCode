# [Python/Go] 模拟

> slug: pythongo-mo-ni-by-himymben-il1d
> date: 2022-01-23
> tags: Go, Python, Python3
> question: Find All Lonely Numbers in the Array (find-all-lonely-numbers-in-the-array)
> url: https://leetcode.cn/problems/find-all-lonely-numbers-in-the-array/solutions/stAal5/pythongo-mo-ni-by-himymben-il1d/

---
### 解题思路
哈希统计即可

### 代码

```python3 []
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        return [c for c in cnts.keys() if cnts[c] == 1 and not cnts[c+1] and not cnts[c-1]] if (cnts := Counter(nums)) else []
```
```go []
func findLonely(nums []int) []int {
    cnts := map[int]int{}
    for _, num := range nums {
        cnts[num]++
    }
    ans := []int{}
    for k, v := range cnts {
        if v == 1 && cnts[k - 1] == 0 && cnts[k + 1] == 0{
            ans = append(ans, k)
        }
    }
    return ans
}
```