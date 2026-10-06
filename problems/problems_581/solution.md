# [Python/Java] Greedy

> Author: Benhao
> Date: 2021-08-03
> Upvotes: 7
> Tags: Java, Python, Python3

---

### Approach
Since we can sort the array only once, we need the leftmost and rightmost positions that violate the required order.
Simply finding the first adjacent inversion from each end is insufficient. In [1,9,1,2,3,4], the right endpoint must be 4. In [1,3,2,2,2], it must be the rightmost 2.
Track the maximum value before each number. If the number is smaller than that maximum, it is out of order.
Likewise, track the minimum value after each number. If the number is larger than that minimum, it is also out of order.

### Code
```Python3 []
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        m, end = -inf, -1
        for i, num in enumerate(nums):
            if num > m:
                m = num
            elif num < m:
                end = i
        if end == -1:
            return 0

        m,start = inf, len(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < m:
                m = nums[i]
            elif nums[i] > m:
                start = i

        return end - start + 1
```
```Java []
class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int m = -10005, end = -1, n = nums.length, start = -1;
        for(int i=0;i<n;i++){
            if(nums[i] > m)
                m = nums[i];
            else if(nums[i] < m)
                end = i;
        }
        if(end < 0)
            return 0;
        m = 10005;
        for(int i=n-1;i>=0;i--){
            if(nums[i] < m)
                m = nums[i];
            else if(nums[i] > m)
                start = i;
        }
        return end - start + 1;

    }
}
```
