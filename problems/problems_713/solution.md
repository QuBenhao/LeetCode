# [Python/Java/JavaScript/Go] Sliding window with two pointers

> slug: pythonjavajavascriptgo-by-himymben-df71
> date: 2022-05-04
> tags: Go, Java, JavaScript, Python, Python3
> question: Subarray Product Less Than K (subarray-product-less-than-k)
> url: https://leetcode.cn/problems/subarray-product-less-than-k/solutions/HSSCCZ/pythonjavajavascriptgo-by-himymben-df71/

---
### Approach
All array elements are positive integers, so extending a product cannot decrease it.
Thus, if a subarray's product is less than k, every subarray within it also qualifies.
For each right endpoint, count the possible left endpoints. This counts every valid subarray ending at that right endpoint at once.

One detail:
Only count subarrays ending at the current right endpoint, since all others were counted earlier.

### Code

```Python3 []
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, left, cur = 0, 0, 1
        for right, num in enumerate(nums):
            cur *= num
            # The product through the right pointer is too large; move the left pointer until it is below k
            while left <= right and cur >= k:
                cur //= nums[left]
                left += 1
            # For every i between left and right, the product of nums[i:right+1] is below k
            ans += right - left + 1
        return ans
```
```Java []
class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int ans = 0, left = 0, cur = 1;
        for(int right = 0; right < nums.length; right++) {
            cur *= nums[right];
            while(left <= right && cur >= k)
                cur /= nums[left++];
            ans += right - left + 1;
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {
    let ans = 0, left = 0, cur = 1
    for(let right = 0; right < nums.length; right++) {
        cur *= nums[right]
        while(left <= right && cur >= k)
            cur /= nums[left++]
        ans += right - left + 1
    }
    return ans
};
```
```Go []
func numSubarrayProductLessThanK(nums []int, k int) (ans int) {
    for left, right, cur := 0, 0, 1; right < len(nums); right++ {
        cur *= nums[right]
        for left <= right && cur >= k {
            cur /= nums[left]
            left++
        }
        ans += right - left + 1
    }
    return
}
```
