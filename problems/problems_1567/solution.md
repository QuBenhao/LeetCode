# [Python/Go] 动态规划

> slug: pythongo-dong-tai-gui-hua-by-himymben-5y64
> date: 2022-02-12
> tags: Go, Python, Python3
> question: Maximum Length of Subarray With Positive Product (maximum-length-of-subarray-with-positive-product)
> url: https://leetcode.cn/problems/maximum-length-of-subarray-with-positive-product/solutions/8e8SJp/pythongo-dong-tai-gui-hua-by-himymben-5y64/

---
### 解题思路
维护正数、负数当前子数组最长的长度

### 代码
```python3 []
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = neg = ans = 0
        for num in nums:
            if num > 0:
                pos += 1
                if neg > 0:
                    neg += 1
            elif num == 0:
                pos = neg = 0
            else:
                if neg > 0:
                    pos, neg = neg + 1, pos + 1
                else:
                    pos, neg = 0, pos + 1
            ans = max(ans, pos)
        return ans
```
```golang []
func getMaxLen(nums []int) (ans int) {
    pos, neg := 0, 0
    for _, num := range nums {
        if num > 0 {
            pos++
            if neg > 0 {
                neg++
            }
        } else if num == 0 {
            pos, neg = 0, 0
        } else {
            if neg > 0 {
                pos, neg = neg + 1, pos + 1
            } else {
                pos, neg = 0, pos + 1
            }
        }
        ans = max(ans, pos)
    }
    return
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```