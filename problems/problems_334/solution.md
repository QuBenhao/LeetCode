# [Python/Java/JavaScript/Go/C] Simplifying the longest increasing subsequence problem

> Author: Benhao
> Date: 2022-01-11
> Upvotes: 40
> Tags: C, Go, Java, JavaScript, Python, Python3

---

### Approach

For LIS (longest increasing subsequence), we often use [a monotonic stack with binary search](https://leetcode.cn/problems/longest-increasing-subsequence/solution/pythonjavajavascriptgo-lis-zui-chang-sha-e36x/).
This problem only requires an increasing subsequence of length 3, so two variables can represent the first two stack entries.
Compare the current number with these two values. If it is smaller than the first, replace the first; otherwise, if it is smaller than the second, replace the second. Otherwise, three suitable numbers have been found.

### Code

```Python3 []
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = mid = inf
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            else:
                return True
        return False
```
```Java []
class Solution {
    public boolean increasingTriplet(int[] nums) {
        int small = Integer.MAX_VALUE, mid = Integer.MAX_VALUE;
        for(int num: nums)
            if(num <= small)
                small = num;
            else if(num <= mid)
                mid = num;
            else
                return true;
        return false;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function(nums) {
    let small = Number.MAX_SAFE_INTEGER, mid = Number.MAX_SAFE_INTEGER
    for(const num of nums)
        if(num <= small)
            small = num
        else if(num <= mid)
            mid = num
        else
            return true
    return false
};
```
```Go []
func increasingTriplet(nums []int) bool {
    small, mid := math.MaxInt32, math.MaxInt32
    for _, num := range nums {
        if num <= small {
            small = num
        } else if num <= mid {
            mid = num
        } else {
            return true
        }
    }
    return false
}
```
```C []
bool increasingTriplet(int* nums, int numsSize){
    int a, b, i;
    a = b = INT_MAX;
    for(i=0;i<numsSize;i++)
        if(nums[i] <= a)a = nums[i];
        else if(nums[i] <= b)b = nums[i];
        else return true;
    return false;
}
```
