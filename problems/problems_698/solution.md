# [Python/Java/TypeScript/Go] 状压dp

> Author: Benhao
> Date: 2022-09-20
> Upvotes: 5
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
[473.火柴拼正方形](https://leetcode.cn/problems/matchsticks-to-square/solution/pythonjavatypescriptgo-by-himymben-57tt/)

### 代码

```Python3 []
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        line = total // k
        if any(num > line for num in nums):
            return False
        n = len(nums)
        final = (1 << n) - 1
        
        @lru_cache(None)
        def dfs(state, cur):
            if cur == line:
                cur = 0
                if state == final:
                    return True
            for i in range(n):
                if not 1 << i & state and cur + nums[i] <= line:
                    if dfs(1 << i | state, cur + nums[i]):
                        return True
            return False
        
        return dfs(0, 0)
```
```Java []
class Solution {
    private Map<Integer, Boolean>[] dp;
    private int n, k, line, allPicked;
    private int[] nums;

    public boolean canPartitionKSubsets(int[] nums_, int k_) {
        nums = nums_;
        n = nums.length;
        k = k_;
        int total = 0;
        for(int v: nums) {
            total += v;
        }
        if (total % k != 0) {
            return false;
        }
        line = total / k;
        for(int v: nums) {
            if (v > line) {
                return false;
            }
        }
        dp = (HashMap<Integer, Boolean>[]) new HashMap[1 << n];
        for(int i = 0; i < 1 << n; i++) {
            dp[i] = new HashMap<Integer, Boolean>();
        }
        allPicked = (1 << n) - 1;
        dp[allPicked].put(0, true);
        return dfs(0, 0);
    }

    private boolean dfs(int state, int cur) {
        if(dp[state].containsKey(cur)) {
            return dp[state].get(cur); 
        }
        for(int i = 0; i < n; i++) {
            if(((state >> i) & 1) == 0 && cur + nums[i] <= line) {
                if(dfs(state | 1 << i, (cur + nums[i]) % line)) {
                    dp[state].put(cur, true);
                    return true;
                }
            }
        }
        dp[state].put(cur, false);
        return false;
    }
}
```
```TypeScript []
function canPartitionKSubsets(nums: number[], k: number): boolean {
    const total = nums.reduce((a, b) => a + b)
    if (total % k != 0) {
        return false
    }
    const n = nums.length, line = Math.floor(total / k)
    for (const num of nums) {
        if (num > line) {
            return false
        }
    }
    const allPicked = (1 << n) - 1
    const dp = new Array(1 << n).fill(-1)
    dp[0] = 0
    for(let i = 0; i <= allPicked; i++) {
        for(let j = 0; j < n; j++) {
            if((i >> j & 1) != 0) {
                const before = i & ~(1 << j)
                if(dp[before] >= 0 && nums[j] + dp[before] <= line) {
                    dp[i] = (dp[before] + nums[j]) % line
                }
            }
        }
    }
    return dp[allPicked] == 0
};
```
```Go []
func canPartitionKSubsets(nums []int, k int) bool {
    total := 0
    for _, v := range nums {
        total += v
    }
    if total % k != 0 {
        return false
    }
    n, line := len(nums), total / k
    for _, v := range nums {
        if v > line {
            return false
        }
    }
    allPicked := (1 << n) - 1
    dp := make([]int, 1 << n)
    for i := 0; i <= allPicked; i++ {
        dp[i] = -1
    }
    dp[0] = 0
    for i := 0; i <= allPicked; i++ {
        for j := 0; j < n; j++ {
            if (i >> j & 1) != 0 {
                before := i & ^(1 << j)
                if dp[before] >= 0 && nums[j] + dp[before] <= line {
                    dp[i] = (nums[j] + dp[before]) % line
                }
            }
        }
    }
    return dp[allPicked] == 0
}
```