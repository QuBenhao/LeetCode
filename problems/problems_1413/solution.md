# [Python/Java/TypeScript/Go] Simulation

> slug: pythonjavatypescriptgo-by-himymben-cxyj
> date: 2022-08-08
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Minimum Value to Get Positive Step by Step Sum (minimum-value-to-get-positive-step-by-step-sum)
> url: https://leetcode.cn/problems/minimum-value-to-get-positive-step-by-step-sum/solutions/FbAMW0/pythonjavatypescriptgo-by-himymben-cxyj/

---
### Approach
Find the minimum prefix sum. The running total must still be at least 1 when it reaches this minimum.

### Code

```Python3 []
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return max(1, 1 - min(accumulate(nums)))
```
```Java []
class Solution {
    public int minStartValue(int[] nums) {
        int presum = 0, ans = 1;
        for (int num: nums) {
            presum += num;
            ans = Math.max(ans, 1 - presum);
        }
        return ans;
    }
}
```
```TypeScript []
function minStartValue(nums: number[]): number {
    let presum = 0, ans = 1
    for (const num of nums) {
        presum += num
        ans = Math.max(ans, 1 - presum)
    }
    return ans
};
```
```Go []
func minStartValue(nums []int) int {
    presum, ans := 0, 1
    for _, num := range nums {
        presum += num
        if d := 1 - presum; d > ans {
            ans = d
        }
    }
    return ans
}
```
