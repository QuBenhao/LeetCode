# [Python/Java/JavaScript/Go] Dynamic programming

> Author: Benhao
> Date: 2022-02-25
> Upvotes: 12
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
Maintain the minimum value seen so far. Pairing it with the current value gives the largest possible difference for that value. Compare these differences and keep the overall maximum.

### Code

```Python3 []
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        m, ans = inf, 0
        for num in nums:
            m, ans = min(num, m), max(ans, num - m)
        return ans if ans > 0 else -1
```
```Java []
class Solution {
    private static final int INF = (int)1e9;
    public int maximumDifference(int[] nums) {
        int m = INF, ans = 0;
        for(int num: nums) {
            ans = Math.max(ans, num - m);
            m = Math.min(m, num);
        }
        return ans > 0 ? ans : -1;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
const INF = 1e9
var maximumDifference = function(nums) {
    let m = INF, ans = 0
    for(const num of nums) {
        ans = Math.max(ans, num - m)
        m = Math.min(m, num)
    }
    return ans > 0 ? ans : -1
};
```
```Go []
const inf int = int(1e9)
func maximumDifference(nums []int) (ans int) {
    m := inf
    for _, num := range nums {
        if num <= m {
            m = num
        } else if d := num - m; d > ans {
            ans = d
        }
    }
    if ans == 0 {
        ans = -1
    }
    return
}
```
