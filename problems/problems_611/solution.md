# [Python/Java] 排序+二分 -> 排序加双指针

> Author: Benhao
> Date: 2021-08-04
> Upvotes: 7
> Tags: Java, Python, Python3

---

### 解题思路
固定较小的两个边，根据三角形两边之和大于第三边这一性质，可以二分查找最大的边的范围。$o(n^2 log_n)$

和上面的思路差不多，但是遍历枚举第二个边再二分查找效率还是比较低。选择枚举最大边，然后双指针搜索能和最大边构成三角形的所有情况。$o(n^2)$
> 为什么不枚举最小边双指针搜剩下两个呢？主要是因为当右端点变小，左端点也是可以变小的而不是一直变大。

### 代码

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
        # 固定最大边, a + b > c
        for i in range(n - 1, 1, -1):
            l, r = 0, i - 1
            # 两数之和问题！
            while l < r:
                # 两数之和大于最大边，他们之间的所有值作为左端点，均可以和右端点构成答案
                if nums[l] + nums[r] > nums[i]:
                    ans += r - l
                    r -= 1
                else:
                    # 小于最大边，构不成答案，之后的右端点都需要更大的左端点才有可能继续构成答案
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
