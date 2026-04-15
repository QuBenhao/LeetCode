# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-10-07
> Upvotes: 10
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
统计所有升序子数组的和，取其中最大即可。

### 代码

```Python3 []
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans, cur = nums[0], nums[0]
        for last, num in pairwise(nums):
            cur = cur + num if last < num else num
            ans = max(ans, cur)
        return ans
```
```Java []
class Solution {
    public int maxAscendingSum(int[] nums) {
        int ans = nums[0], cur = nums[0];
        for (int i = 1; i < nums.length; i++) {
            cur = nums[i] > nums[i - 1] ? cur + nums[i] : nums[i];
            ans = Math.max(ans, cur);
        }
        return ans;
    }
}
```
```TypeScript []
function maxAscendingSum(nums: number[]): number {
    let ans: number = nums[0], cur: number = nums[0]
    for (let i = 1; i < nums.length; i++) {
        cur = nums[i] > nums[i - 1] ? cur + nums[i] : nums[i]
        ans = Math.max(ans, cur)
    }
    return ans
};
```
```Go []
func maxAscendingSum(nums []int) (ans int) {
    last, cur := 0, 0
    for _, num := range nums {
        if num > last {
            cur += num
        } else {
            cur = num
        }
        if cur > ans {
            ans = cur
        }
        last = num
    }
    return
}
```