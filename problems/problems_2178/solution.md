# [Python/Go] 贪心

> slug: pythongo-tan-xin-by-himymben-gnyi
> date: 2022-02-20
> tags: Go, Python, Python3
> question: Maximum Split of Positive Even Integers (maximum-split-of-positive-even-integers)
> url: https://leetcode.cn/problems/maximum-split-of-positive-even-integers/solutions/YL24Iz/pythongo-tan-xin-by-himymben-gnyi/

---
### 解题思路
从小到大取不同的偶数直到和大于等于最终结果。
如果等于直接返回，大于的话将最后一个元素变大直接到和为答案即可。（贪心保证了个数最多）

### 代码

```Python3 []
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        total, ans = 0, [2]
        while total < finalSum:
            total += ans[-1]
            ans.append(ans[-1] + 2)
        ans.pop()
        if total == finalSum:
            return ans
        return ans[:-2] + [finalSum - sum(ans[:-2])]
```
```Go []
func maximumEvenSplit(finalSum int64) (ans []int64) {
    if finalSum & 1 == 0 {
        for i := int64(2); i <= finalSum; i += 2 {
            ans = append(ans, i)
            finalSum -= i
        }
        ans[len(ans) - 1] += finalSum
    }
    return
}
```