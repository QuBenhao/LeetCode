# [Python/Java/JavaScript/Go] 抽屉原理

> Author: Benhao
> Date: 2022-05-21
> Upvotes: 11
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
把2n个位置看成n个装两个数的抽屉。
由于有n个相同的数，那么要么他们各自在一个抽屉中(相隔)，要么存在一对儿在一个抽屉中(相邻)。

假设我们不存在相邻的相同数(即所有相同数都被隔开)，
只有在n=2的时候，可以出现一个在头一个在尾中间隔着两个数的情况，其他情况都一定存在某两个相同数最多隔一个其他数。

处理掉这一个特殊情况，我们循环判断相邻和相隔一个位置的数是否相等即可。

### 代码

```Python3 []
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        if nums[0] == nums[3]:
            return nums[0]
        for i, num in enumerate(nums):
            if nums[i + 1] == num or nums[i + 2] == num:
                return num
        return -1
```
```Java []
class Solution {
    public int repeatedNTimes(int[] nums) {
        if(nums[0] == nums[3]) {
            return nums[0];
        }
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == nums[i + 1] || nums[i] == nums[i + 2]) {
                return nums[i];
            }
        }
        return -1;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var repeatedNTimes = function(nums) {
    if(nums[0] == nums[3]) {
        return nums[0]
    }
    for(let i = 0; i < nums.length; i++) {
        if(nums[i] == nums[i + 1] || nums[i] == nums[i + 2]) {
            return nums[i]
        }
    }
    return -1
};
```
```Go []
func repeatedNTimes(nums []int) int {
    if nums[0] == nums[3] {
        return nums[0]
    }
    for i := 0; i < len(nums); i++ {
        if nums[i + 1] == nums[i] || nums[i + 2] == nums[i] {
            return nums[i]
        }
    }
    return -1
}
```