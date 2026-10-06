# [Python/Java/JavaScript/Go] Pigeonhole principle

> Author: Benhao
> Date: 2022-05-21
> Upvotes: 11
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
Treat the 2n positions as n drawers holding two numbers each.
The n equal numbers either occupy separate drawers or include a pair sharing a drawer, making them adjacent.

Suppose there are no adjacent equal numbers, so every copy is separated.
Only when n=2 can one copy be first and the other last with two numbers between them. In every other case, some pair of equal numbers has at most one other number between them.

Handle this special case, then check equal values at adjacent positions and positions two apart.

### Code

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
