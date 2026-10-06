# [Python/Java/Go] Dynamic programming or two pointers

> Author: Benhao
> Date: 2021-08-09
> Upvotes: 20
> Tags: Go, Java, Python, Python3

---

### Approach
Happy Birthday~!
<br>
An arithmetic sequence has equal differences between adjacent elements. One approach checks whether the current difference matches the previous difference. If so, the current and previous two values form an arithmetic sequence. Any earlier arithmetic sequence ending at the previous value can also be extended. Thus, a sequence of length k ending at the previous value becomes one of length k+1.
Starting from any of the previous k values and ending at the current value gives an arithmetic sequence. Each one of length at least 3 contributes a distinct answer.

Another approach finds the longest contiguous arithmetic sequence with a fixed difference. If its length is k, count all subarrays of length at least 3: there are k-2 of length 3, k-3 of length 4, and so on. Their sum is $1+2+3+\dots+k-2 = (k-1)*(k-2)/2$.

The first approach simply expands this summation and adds the terms one by one.


### Code

```Python3 []
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        # Previous difference
        last = None
        # Length of the preceding run of equal differences
        last_len = ans = 0
        for i in range(1, n):
            # Equal difference: extend the run by one
            if nums[i] - nums[i-1] == last:
                last_len += 1
            # Otherwise, the run contains only the difference between these two values
            else:
                last_len = 1
            # This contributes len-1 possibilities ending here
            ans += last_len - 1
            last = nums[i] - nums[i-1]
        return ans
```
```Java []
class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int n = nums.length, last_len = 0, ans = 0, last = 2001;
        for(int i=1;i<n;i++){
            if(nums[i]-nums[i-1] == last)
                last_len++;
            else
                last_len = 1;
            ans += last_len - 1;
            last = nums[i] - nums[i-1];
        }
        return ans;
    }
}
```
```Go []
func numberOfArithmeticSlices(nums []int) (ans int) {
    if len(nums) <= 2 {
        return 0
    }
    d, l := nums[1] - nums[0], 0
    for i, num := range nums[2:] {
        if nd := num - nums[i + 1]; nd == d {
            l++
            ans += l
        } else {
            d = nd
            l = 0
        }
    }
    return
}
```

Approach 2
```Python3 []
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = ans = 0
        # At l = n-2, too few values remain to form another arithmetic sequence
        while l < n - 2:
            d = nums[l + 1] - nums[l]
            while r < n - 1 and nums[r + 1] - nums[r] == d:
                r += 1
            # k = r - l + 1, (k-1)*(k-2)/2 = (r-l) * (r-l-1)/2
            ans += (r-l) *(r-l-1)//2
            l = r
        return ans
```
```Java []
class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int n = nums.length, ans = 0;
        for(int l=0,r=0;l < n - 2;){
            int d = nums[l+1] - nums[l];
            while(r < n - 1 && nums[r+1] - nums[r] == d)
                r++;
            ans += (r-l) * (r-l-1) / 2;
            l = r;
        }
        return ans;
    }
}
```
