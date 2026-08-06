# [Python/Java/JavaScript/Go] 双指针滑窗

> slug: pythonjavajavascriptgo-by-himymben-df71
> date: 2022-05-04
> tags: Go, Java, JavaScript, Python, Python3
> question: Subarray Product Less Than K (subarray-product-less-than-k)
> url: https://leetcode.cn/problems/subarray-product-less-than-k/solutions/HSSCCZ/pythonjavajavascriptgo-by-himymben-df71/

---
### 解题思路
数组中的数全部为正数，乘法为非递减，
也就是说一段乘积小于k的子数组中，所有的子数组都满足答案。
我们只需要找对于每个右指针，其左指针的个数有多少个（可选范围），就可以一次性统计以该右指针作为结尾的所有子数组个数。

一个细节：
仅统计右指针的左指针范围是因为其他子数组已经在前面计算过了。

### 代码

```Python3 []
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, left, cur = 0, 0, 1
        for right, num in enumerate(nums):
            cur *= num
            # 当前到右指针的连乘太大，需要一直挪动左指针直到小于k
            while left <= right and cur >= k:
                cur //= nums[left]
                left += 1
            # 在left到right之间的i, nums[i:right+1]的连乘都满足小于k
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