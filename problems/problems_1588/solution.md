# [Python/Java] Inclusion-exclusion: o(n) time, o(1) space

> Author: Benhao
> Date: 2021-08-28
> Upvotes: 26
> Tags: Java, Python, Python3

---

### Approach
Reframe the problem as counting the odd-length subarrays containing each number: how many times does each number contribute? For the first number, this depends on the total length; it appears in exactly `(length + 1) // 2` odd-length subarrays.
Can the count for one number be derived from the previous number's count?
Every subarray of length 3, 5, 7, and so on containing the first number also contains the second, but the length-1 subarray does not.
Likewise, subarrays starting at the second number do not contain the first.
The second number's count equals `the first number's count`, minus `the count containing the first but not the second`, plus `the count containing the second but not the first`.
We can keep track of the previous number's count.
How many subarrays contain the previous number but not the current one? Apply the same idea recursively: count odd-length subarrays within 0 through i-1 that contain i-1, using the interval length.
Similarly, subarrays containing the current number but not the previous one lie within i through n-1 and contain i; their count also follows from the interval length.

This gives the following facts:
> The first position appears (n+1)//2 times.
> The current position appears (n - i + 1) // 2 - (i + 1) // 2 more times than the previous one.
> Positions mirrored across the array have equal counts by symmetry.

You can also apply this recurrence from start to finish without using two pointers.

### Code

```Python3 []
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # How many odd-length subarrays of an array of length n contain the first position?
        # 1, 3, 5, ..., length-1/length
        # (length + 1)//2
        n = len(arr)
        l, r, ans, times = 0, n - 1, 0, (n+1) // 2
        while l <= r:
            # By symmetry, mirrored positions have equal counts
            if l < r:
                ans += times * (arr[l] + arr[r])
            else:
                ans += times * arr[l]
            l += 1
            r -= 1
            # Add odd-length subarrays containing the next number but not the previous one
            times += (n - l + 1) // 2 
            # Subtract odd-length subarrays containing the previous number but not the next one
            times -= (l + 1) // 2
        return ans
```
```Java []
class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int n = arr.length;
        int ans = 0;
        for(int l = 0, r = n - 1, times = (n + 1)/2; l<=r; r--){
            if(l < r)
                ans += times * (arr[l] + arr[r]);
            else
                ans += times * arr[l];
            times += (n-++l+1)/2 - (l+1)/2;
        }
        return ans;
    }
}
```
