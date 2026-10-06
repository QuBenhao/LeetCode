# [Python/Go] Greedy

> slug: pythongo-tan-xin-by-himymben-gnyi
> date: 2022-02-20
> tags: Go, Python, Python3
> question: Maximum Split of Positive Even Integers (maximum-split-of-positive-even-integers)
> url: https://leetcode.cn/problems/maximum-split-of-positive-even-integers/solutions/YL24Iz/pythongo-tan-xin-by-himymben-gnyi/

---
### Approach
Take distinct even numbers in increasing order until their sum reaches or exceeds the target.
If the sum equals the target, return it. Otherwise, enlarge the last selected element to make the sum equal the target. (The greedy choice maximizes the number of elements.)

### Code

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
