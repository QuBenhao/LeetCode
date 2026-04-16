# [Python/Java] 前缀和+二分查找 

> Author: Benhao
> Date: 2021-09-09
> Upvotes: 7
> Tags: Java, Python, Python3

---

### 解题思路
首先根据消耗粉笔是循环的，所以我们可以用消耗粉笔的和对k进行取余，结果保持一致(相当于取了很多轮以后)。
根据余数，我们需要判断到哪个学生会消耗完。而这正是前缀和中找余数的位置(二分加速)。

### 代码

```Python3 []
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        return bisect_right((presum := list(accumulate(chalk))), k % presum[-1])
```
```Java []
class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        int n = chalk.length;
        long[] presum = new long[n];
        for(int i=0;i<n;i++)
            presum[i] = chalk[i] + (i > 0 ? presum[i-1] : 0);
        k %= presum[n-1];
        int l = 0, r = n - 1;
        while(l < r){
            int mid = l + r >> 1;
            if(presum[mid] <= k)
                l = mid + 1;
            else
                r = mid;
        }
        return l;
    }
}
```
