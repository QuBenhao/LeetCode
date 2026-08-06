# [Python/Go] 模拟

> slug: pythongo-mo-ni-by-himymben-xcy7
> date: 2022-02-13
> tags: Go, Python, Python3
> question: Minimum Operations to Make the Array Alternating (minimum-operations-to-make-the-array-alternating)
> url: https://leetcode.cn/problems/minimum-operations-to-make-the-array-alternating/solutions/CuvQbT/pythongo-mo-ni-by-himymben-xcy7/

---
### 解题思路
统计奇偶坐标的最多元素和次多元素

### 代码

```Python3 []
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def helper(start):
            cnts = Counter(nums[start::2])
            m, mCnts, sm, smCnts = None, 0, None, 0
            for k, v in cnts.items():
                if v > mCnts:
                    m, mCnts, sm, smCnts = k, v, m, mCnts
                elif v == mCnts or v > smCnts:
                    sm, smCnts = k, v
            return m, mCnts, sm, smCnts
        
        evens, odds = helper(0), helper(1)
        if odds[0] != evens[0]:
            return len(nums) - evens[1] - odds[1]
        return min(len(nums) - evens[1] - odds[3], len(nums) - evens[3] - odds[1])
```
```Go []
func minimumOperations(nums []int) int {
    helper := func(idx int) []int {
        cnts, m, mCnts, sm, smCnts := map[int]int{}, 0, 0, 0, 0
        for ; idx < len(nums); idx += 2 {
            cnts[nums[idx]] += 1
        }
        for k, v := range cnts {
            if v > mCnts {
                m, mCnts, sm, smCnts = k, v, m, mCnts
            } else if v == mCnts || v > smCnts {
                sm, smCnts = k, v
            }
        }
        return []int{m, mCnts, sm, smCnts}
    }
    
    evens, odds := helper(0), helper(1)
    if evens[0] != odds[0] {
        return len(nums) - evens[1] - odds[1]
    }
    a, b := len(nums) - evens[3] - odds[1], len(nums) - odds[3] - evens[1]
    if a > b {
        return b
    }
    return a
}
```