# [Python/Java] 暴力模拟

> Author: Benhao
> Date: 2021-08-22
> Upvotes: 3
> Tags: Java, Python, Python3

---

### 解题思路
按步长为2遍历数组(所有偶数位)，该位和该位的下一个奇数位按规则填入，返回最大值即可。

### 代码

```Python3 []
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1, 2):
            nums[i] = nums[i//2]
            if i < n:
                nums[i+1] = nums[i//2] + nums[i//2 + 1]
        return max(nums)
```
```Java []
class Solution {
    public int getMaximumGenerated(int n) {
        if(n==0)
            return 0;
        int[] nums = new int[n+1];
        nums[1] = 1;
        int ans = 1;
        for(int i=2;i<n+1;i+=2){
            nums[i] = nums[i/2];
            if(i < n){
                nums[i+1] = nums[i/2] + nums[i/2 + 1];
                ans = Math.max(ans, nums[i+1]);
            }
        }
        return ans;
    }
}
```
```Java []
class Solution {
    public int getMaximumGenerated(int n) {
        if(n==0)
            return 0;
        int[] nums = new int[n+1];
        nums[1] = 1;
        int ans = 1;
        for(int i=2;i<n+1;i++){
            nums[i] = nums[i/2];
            if(i < n){
                nums[++i] = nums[i/2] + nums[i/2 + 1];
                ans = Math.max(ans, nums[i]);
            }
        }
        return ans;
    }
}
```