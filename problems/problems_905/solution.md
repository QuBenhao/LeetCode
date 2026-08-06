# [Python/Java/JavaScript/Go] 模拟

> slug: python-by-himymben-c1j5
> date: 2022-04-27
> tags: Go, Java, JavaScript, Python, Python3
> question: Sort Array By Parity (sort-array-by-parity)
> url: https://leetcode.cn/problems/sort-array-by-parity/solutions/GI1w72/python-by-himymben-c1j5/

---
### 解题思路
该用户太懒了只有代码

### 代码
```python3
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return list(chain(filterfalse(lambda x:x%2, nums), filterfalse(lambda x:1^x%2, nums)))
```
```python3
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x:x%2)
```
```Python3 []
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and not nums[l] % 2:
                l += 1
            while r > l and nums[r] % 2:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        return nums
```
```Java []
class Solution {
    public int[] sortArrayByParity(int[] nums) {
        for(int l = 0, r = nums.length - 1; l < r; ) {
            while(l < r && nums[l] % 2 == 0) l++;
            while(r > l && nums[r] % 2 == 1) r--;
            if(l < r) {
                int tmp = nums[l];
                nums[l] = nums[r];
                nums[r] = tmp;
            }
        }
        return nums;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
    for(let l = 0, r = nums.length - 1; l < r; ) {
        while(l < r && nums[l] % 2 == 0)
            l++
        while(r > l && nums[r] % 2 == 1)
            r--
        if(l < r) {
            const tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
        }
    }
    return nums
};
```
```Go []
func sortArrayByParity(nums []int) []int {
    for l, r := 0, len(nums) - 1; l < r; {
        for l < r && nums[l] % 2 == 0 {
            l++
        }
        for r > l && nums[r] % 2 == 1 {
            r--
        }
        nums[l], nums[r] = nums[r], nums[l]
    }
    return nums
}
```