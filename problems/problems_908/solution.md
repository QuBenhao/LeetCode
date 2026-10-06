# [Python/Java/JavaScript/Go] Mathematics

> Author: Benhao
> Date: 2022-04-29
> Upvotes: 23
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
To minimize the score, reduce the difference between the array's maximum and minimum.
Make the maximum as small as possible and the minimum as large as possible to reduce their difference, noting that the final maximum is at least the final minimum.

If the maximum $nums_i$ and minimum $nums_j$ can reach a common value, every number can reach it and the answer is 0. ($nums_i - k \le nums_j + k$)
If the smallest possible maximum ($nums_i-k$) still exceeds the largest possible minimum ($nums_j+k$), the answer, or minimum score, is $nums_i-nums_j-2*k$. ($nums_i - k \gt nums_j + k$)

### Code

```Python3 []
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)
```
```Java []
class Solution {
    public int smallestRangeI(int[] nums, int k) {
        int max = 0, min = 10001;
        for(int num: nums) {
            max = Math.max(num, max);
            min = Math.min(num, min);
        }
        return Math.max(0, max - min - 2 * k);
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var smallestRangeI = function(nums, k) {
    let max = 0, min = 10001
    for(const num of nums) {
        max = Math.max(num, max)
        min = Math.min(num, min)
    }
    return Math.max(0, max - min - 2 * k)
};
```
```Go []
func smallestRangeI(nums []int, k int) int {
    max, min := 0, 10001
    for _, num := range nums {
        if num > max {
            max = num
        }
        if num < min {
            min = num
        }
    }
    if v := max - min - 2 * k; v >= 0 {
        return v
    }
    return 0
}
```
