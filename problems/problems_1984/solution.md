# [Python/Java/JavaScript/Go] Sorting + two-pointer sliding window

> Author: Benhao
> Date: 2022-02-10
> Upvotes: 20
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
After sorting, the k values with the smallest maximum-minus-minimum difference form a contiguous length-k subarray. Its difference is the rightmost value minus the leftmost value.
Enumerate these windows and return the smallest difference.

### Code

```Python3 []
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        return min(s[i + k - 1] - s[i] for i in range(len(s) - k + 1)) if k > 1 and (s:=sorted(nums)) else 0
```
```Java []
class Solution {
    public int minimumDifference(int[] nums, int k) {
        if(k == 1)
            return 0;
        Arrays.sort(nums);
        int ans = 100005;
        for(int i = 0; i <= nums.length - k; i++)
            ans = Math.min(ans, nums[i + k - 1] - nums[i]);
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
var minimumDifference = function(nums, k) {
    if(k == 1)
        return 0
    nums.sort((a,b)=>a-b)
    let ans = 100005
    for(let i = 0; i <= nums.length - k; i++)
        ans = Math.min(ans, nums[i + k - 1] - nums[i])
    return ans
};
```
```Go []
func minimumDifference(nums []int, k int) int {
    if k == 1 {
        return 0
    }
    sort.Ints(nums)
    ans := 100005
    for i := 0; i <= len(nums) - k; i++ {
        ans = min(ans, nums[i + k - 1] - nums[i])
    }
    return ans
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```
