# [Python/Java/JavaScript/Go] LIS 最长上升子序列模板

> Author: Benhao
> Date: 2022-01-11
> Upvotes: 11
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
利用单调栈 + 二分查找实现o(nlogn)解法

### 代码

```Python3 []
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            idx = bisect_left(stack, num)
            if idx == len(stack):
                stack.append(num)
            else:
                stack[idx] = num
        return len(stack)
```
```Java []
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] stack = new int[nums.length];
        int idx = 0;
        for(int i=0;i<nums.length;i++){
            int num = nums[i], l = 0, r = idx;
            while(l < r){
                int mid = (l + r)/2;
                if(stack[mid] < num)
                    l = mid + 1;
                else
                    r = mid;
            }
            if(l == idx)
                stack[idx++] = num;
            else
                stack[l] = num;
        }
        return idx;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    const stack = new Array(nums.length)
    let idx = 0
    for(const num of nums){
        let l = 0, r = idx
        while(l < r){
            let mid = Math.floor((l+r)/2)
            if(stack[mid] < num)
                l = mid + 1
            else
                r = mid
        }
        if(l == idx)
            stack[idx++] = num
        else
            stack[l] = num
    }
    return idx
};
```
```Go []
func lengthOfLIS(nums []int) int {
    stack := []int{}
    for _, num := range nums {
        l := 0
        for r := len(stack); l < r; {
            mid := (l + r) / 2
            if stack[mid] >= num {
                r = mid
            } else {
                l = mid + 1
            }
        }
        if l == len(stack) {
            stack = append(stack, num)
        } else {
            stack[l] = num
        }
    }
    return len(stack)
}
```