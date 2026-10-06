# [Python/Java] Sorting + binary search -> sorting + two pointers

> Author: Benhao
> Date: 2021-08-04
> Upvotes: 7
> Tags: Java, Python, Python3

---

### Approach
Fix the two smaller sides. Since the sum of two sides must exceed the third, binary search for the range of possible largest sides. $o(n^2 log_n)$

The idea is similar, but enumerating the second side and binary searching is relatively slow. Instead, enumerate the largest side and use two pointers to find every pair that forms a triangle with it. $o(n^2)$
> Why not enumerate the smallest side and use two pointers for the other two? As the right endpoint decreases, the left endpoint may also need to decrease instead of always increasing.

### Code

```Python3 []
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n - 2):
            for j in range(i+1, n - 1):
                idx = bisect.bisect_left(nums, nums[i] + nums[j])
                if idx > j:
                    ans += idx - 1 - j
        return ans 
```
```Java []
class Solution {
    public int triangleNumber(int[] nums) {
        int n = nums.length, ans = 0;
        Arrays.sort(nums);
        for(int i=0;i<n-2;i++){
            for(int j=i+1;j<n-1;j++){
                int idx = binarySearch(nums, nums[i] + nums[j], j);
                ans += idx - j;
            }
        }
        return ans;
    }

    public int binarySearch(int[] nums, int target, int left){
        int l = left, r = nums.length - 1;
        while(l < r){
            int mid = (l + r + 1) / 2;
            if(nums[mid] < target)
                l = mid;
            else
                r = mid - 1;
        }
        return l;
    }
}
```
<br>
```Python3 []
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        # Fix the largest side, a + b > c
        for i in range(n - 1, 1, -1):
            l, r = 0, i - 1
            # This is a two-sum problem!
            while l < r:
                # If the sum exceeds the largest side, every left endpoint between the pointers also works with this right endpoint
                if nums[l] + nums[r] > nums[i]:
                    ans += r - l
                    r -= 1
                else:
                    # If the sum is too small, later right endpoints need a larger left endpoint to form a valid triangle
                    l += 1
        return ans
```
```Java []
class Solution {
    public int triangleNumber(int[] nums) {
        int n = nums.length, ans = 0;
        Arrays.sort(nums);
        for(int i=n-1;i>=2;i--)
            for(int l = 0,r = i - 1;l<r;){
                if(nums[l] + nums[r] <= nums[i])
                    l++;
                else{
                    ans += r - l;
                    r--;
                }
            }
        return ans;
    }
}
```
