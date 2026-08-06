# [Python/Go] 模拟

> slug: pythongo-mo-ni-by-himymben-bxz8
> date: 2022-01-23
> tags: Go, Python, Python3
> question: Rearrange Array Elements by Sign (rearrange-array-elements-by-sign)
> url: https://leetcode.cn/problems/rearrange-array-elements-by-sign/solutions/AXsGBz/pythongo-mo-ni-by-himymben-bxz8/

---
### 解题思路
双指针模拟或直接模拟均可

### 代码

```python3 []
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans, i, j = [0] * len(nums), 0, 1
        for num in nums:
            if num > 0:
                ans[i] = num
                i += 2
            else:
                ans[j] = num
                j += 2
        return ans
```
```Go []
func rearrangeArray(nums []int) []int {
    ans := make([]int, len(nums))
    i, j := 0, 1
    for _, num := range nums {
        if num > 0 {
            ans[i] = num
            i += 2
        } else {
            ans[j] = num
            j += 2
        }
    }
    return ans
}
```

```python3 
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        ans = []
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans
```