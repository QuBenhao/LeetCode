# [Python/Java] 贪心

> Author: Benhao
> Date: 2021-08-03
> Upvotes: 7
> Tags: Java, Python, Python3

---

### 解题思路
因为我们只能给数组排序一次，所以我们必然需要找最左和最右的大小关系相反的地方。
单纯地找第一个大小不等的地方(前后)是不合理的。比如[1,9,1,2,3,4], 我们要认定最右为4。而[1,3,2,2,2]，我们要认定最右为最右边的2。
我们需要知道一个数前面的最大值，如果它小于这个最大值，那么它的顺序肯定是不合理的。
同理,我们需要知道一个数后面的最小值，如果它大于这个最小值，那么它的顺序同样是不合理的。

### 代码
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
