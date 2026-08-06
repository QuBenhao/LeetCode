# [Python/Java/JavaScript/Go] 前缀和 + 背包动态规划

> slug: pythonjavajavascriptgo-qian-zhui-he-bei-3mfqv
> date: 2021-12-07
> tags: Go, Java, JavaScript, Python, Python3
> question: Maximum Sum of 3 Non-Overlapping Subarrays (maximum-sum-of-3-non-overlapping-subarrays)
> url: https://leetcode.cn/problems/maximum-sum-of-3-non-overlapping-subarrays/solutions/XAuD8f/pythonjavajavascriptgo-qian-zhui-he-bei-3mfqv/

---
### 解题思路
我们先预处理获得所有长度为k的子数组的和
对于这里面的所有和，我们要取不能相邻k个内的三个，和最大的值
说白了就是每k个最多取一个，跟打家劫舍的背包大同小异，只是需要记录路径的坐标
我们用动态规划，分别维护当前取第一个的最大值和坐标，取第二个的最大值和坐标和取第三个的最大值和坐标即可

### 代码

```Python3 []
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        def lMax(l1, l2):
            # 根据我们放入这个函数的顺序，可以保证相等的时候我们始终返回坐标字典序小的那一个
            if l1[0] >= l2[0]:
                return l1
            return l2

        presum = [0] + list(accumulate(nums))
        # 每k个求和构成所有可选的连续子数组的和
        windows = [presum[i+k] - presum[i] for i in range(len(nums) - k + 1)]
        # 从windows里选三个数和最大且不相邻
        # dp[i]有三个维度，分别代表选第一个的最大值和坐标，选第二个的最大值和坐标，以及选第三个的最大值和坐标
        dp = [[[0, -1]] * 3 for _ in range(len(windows))]
        for i,w in enumerate(windows):
            # 只有可能选第一个
            if i < k:
                dp[i][0] = lMax(dp[i-1][0], [w, i])
            else:
                dp[i][0] = lMax(dp[i-1][0], [w, i])
                # 维护第二个的最大值, 它由k个前取了第一个的最大值加上取当前的值 和 上一次取第二个的最大值构成
                dp[i][1] = lMax([dp[i-k][0][0] + w, (dp[i-k][0][1],i)], dp[i-1][1])
                # 只有2k以后才有可能选第三个，维护第三个的最大值, 它由k个前取了第二个的最大值加上取当前的值 和 上一次取第三个的最大值构成
                if i >= 2 * k:
                    dp[i][2] = lMax([dp[i-k][1][0] + w, (dp[i-k][1][1][0],dp[i-k][1][1][1],i)], dp[i-1][2])
        m, ans = 0, None
        for d in dp:
            if d[2][0] > m:
                m = d[2][0]
                ans = d[2][1]
        return ans
```
```Java []
class Solution {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int[] windows = new int[nums.length - k + 1];
        for(int i=0,j=0,s=0;i<=nums.length;i++){
            if(i < k)
                s += nums[i];
            else{
                windows[j++] = s;
                if(i<nums.length)
                    s += nums[i] - nums[i-k];
            }
        }
        int[][][] dp = new int[windows.length][3][1];
        for(int i=0;i<windows.length;i++)
            if(i < k)
                if(i > 0)
                    dp[i][0] = lMax(new int[]{windows[i], i}, dp[i-1][0]);
                else
                    dp[i][0] = new int[]{windows[i], i};
            else{
                dp[i][0] = lMax(new int[]{windows[i], i}, dp[i-1][0]);
                dp[i][1] = lMax(new int[]{dp[i-k][0][0]+windows[i], dp[i-k][0][1], i}, dp[i-1][1]);
                if(i >= 2 * k)
                    dp[i][2] = lMax(new int[]{dp[i-k][1][0] + windows[i], dp[i-k][1][1], dp[i-k][1][2], i}, dp[i-1][2]);
            }
        int m = 0;
        int[] ans = new int[3];
        for(int i=0;i<windows.length;i++)
            if(dp[i][2][0] > m){
                m = dp[i][2][0];
                for(int j=0;j<3;j++)
                    ans[j] = dp[i][2][j+1];
            }
        return ans;
    }

    private int[] lMax(int[] a, int[] b){
        if(a[0] > b[0])
            return a;
        return b;
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSumOfThreeSubarrays = function(nums, k) {
    var lMax = function(l1, l2){
        if(l1[0] > l2[0])
            return l1
        return l2
    }

    const windows = new Array(nums.length - k + 1)
    for(let i=0,j=0,s=0;i<=nums.length;i++){
        if(i < k)
            s += nums[i]
        else{
            windows[j++] = s
            if(i<nums.length)
                s += nums[i] - nums[i-k]
        }
    }
    const dp = new Array(windows.length)
    for(let i=0;i<dp.length;i++){
        dp[i] = new Array(3)
        for(let j=0;j<3;j++)
            dp[i][j] = [0]
    }
        
    for(let i=0;i<windows.length;i++)
        if(i < k)
            if(i > 0)
                dp[i][0] = lMax([windows[i], i], dp[i-1][0])
            else
                dp[i][0] = [windows[i], i]
        else{
            dp[i][0] = lMax([windows[i], i], dp[i-1][0])
            dp[i][1] = lMax([dp[i-k][0][0]+windows[i], dp[i-k][0][1], i], dp[i-1][1])
            if(i >= 2 * k)
                dp[i][2] = lMax([dp[i-k][1][0] + windows[i], dp[i-k][1][1], dp[i-k][1][2], i], dp[i-1][2])
        }
    let m = 0;
    let ans = new Array(3);
    for(let i=0;i<windows.length;i++)
        if(dp[i][2][0] > m){
            m = dp[i][2][0];
            for(let j=0;j<3;j++)
                ans[j] = dp[i][2][j+1];
        }
    return ans;
};
```
```Go []
func maxSumOfThreeSubarrays(nums []int, k int) []int {
    type path struct{
        Val, A, B, C int
    }
    max := func(a,b path) path {
        if a.Val > b.Val {
            return a
        }
        return b
    }

    windows := make([]int, len(nums) - k + 1)
    for i,j,s :=0,0,0; i <= len(nums); i++ {
        if i < k {
            s += nums[i]
        }else{
            windows[j] = s
            j++
            if i < len(nums) {
                s += nums[i] - nums[i - k]
            }
        }
    }

    dp := make([][]path, len(nums) - k + 1)
    for i := 0; i < len(windows); i++{
        dp[i] = make([]path, 3)
        if i == 0 {
            dp[i][0] = path{windows[i], i, 0, 0}
        }else{
            dp[i][0] = max(path{windows[i], i, 0, 0},dp[i-1][0])
        }
        if i >= k {
            dp[i][1] = max(path{dp[i-k][0].Val + windows[i], dp[i-k][0].A, i, 0}, dp[i-1][1])
            if i >= 2 * k {
                dp[i][2] = max(path{dp[i-k][1].Val + windows[i], dp[i-k][1].A,dp[i-k][1].B, i}, dp[i-1][2]) 
            }
        }
    }
    p := path{0, 0, 0, 0}
    for _, paths := range dp {
        if paths[2].Val > p.Val{
            p = paths[2]
        }
    }
    return []int{p.A, p.B, p.C}
}
```