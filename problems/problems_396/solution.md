# [Python/Java/JavaScript/Go] 找到相邻递推关系

> slug: pythonjavajavascriptgo-by-himymben-anmd
> date: 2022-04-21
> tags: Go, Java, JavaScript, Python, Python3
> question: Rotate Function (rotate-function)
> url: https://leetcode.cn/problems/rotate-function/solutions/VfSick/pythonjavajavascriptgo-by-himymben-anmd/

---
### 解题思路
不难发现：
$F(k + 1) = F(k) + \sum_{i=0}^{n-1}nums_i - n * nums_{-k}$
我们从F(0)出发，遍历所有F，统计最大值

### 代码

```Python3 []
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # F(k + 1) = F(k) + sum(nums) - n * nums[-k]
        n, s, f = len(nums), sum(nums), sum(i * num for i, num in enumerate(nums))
        ans = f
        for i in range(1, n):
            f += s - n * nums[-i]
            ans = max(ans, f)
        return ans
```
```Java []
class Solution {
    public int maxRotateFunction(int[] nums) {
        int f = 0, n = nums.length, s = 0;
        for(int i = 0; i < nums.length; i++) {
            s += nums[i];
            f += i * nums[i];
        }
        int ans = f;
        for(int i = n - 1; i > 0; i--) {
            f = f - n * nums[i] + s;
            ans = Math.max(ans, f);
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxRotateFunction = function(nums) {
    const n = nums.length
    let f = 0, s = 0
    for(let i = 0; i < n; i++) {
        f += i * nums[i]
        s += nums[i]
    }
    let ans = f
    for(let i = n - 1; i > 0; i--) {
        f += s - n * nums[i]
        ans = Math.max(ans, f)
    }
    return ans
};
```
```Go []
func maxRotateFunction(nums []int) int {
    f, s, n := 0, 0, len(nums)
    for i := 0; i < n; i++ {
        f += i * nums[i]
        s += nums[i]
    }
    ans := f
    for i := n - 1; i > 0; i-- {
        f += s - n * nums[i]
        if f > ans {
            ans = f
        }
    }
    return ans
}
```