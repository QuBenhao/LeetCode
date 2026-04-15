# [Python/Java/JavaScript/Go/C] 简化最长上升子序列问题

> Author: Benhao
> Date: 2022-01-11
> Upvotes: 40
> Tags: C, Go, Java, JavaScript, Python, Python3

---

### 解题思路

在求解LIS（最长上升子序列时，我们常用[单调栈维护+二分查找实现](https://leetcode.cn/problems/longest-increasing-subsequence/solution/pythonjavajavascriptgo-lis-zui-chang-sha-e36x/)）。
本题只需要找到任意一个长度等于3的上升子序列，故可以用两个变量模拟前两个栈内元素，
判断当前数字在跟这两个元素的大小关系，如果小于第一个，则替换第一个，然后如果小于第二个，则替换第二个，否则我们已经找到了满足答案的三个数。

### 代码

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
