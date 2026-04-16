# [Python/Java/JavaScript/Go] 简单递归模拟

> Author: Benhao
> Date: 2022-03-14
> Upvotes: 21
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
1. $a | b \geq a$, $a | b \geq b$， 所以最终最大的或结果为全部数字的或（因为或操作是非递减的）
2. 我们知道最大的或结果，只需统计有多少种子集能构成这个结果即可

### 代码

```Python3 []
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        m, n = 0, len(nums)
        for num in nums:
            m |= num
        
        def dfs(idx, val):
            if idx == n:
                return int(val == m)
            return dfs(idx + 1, val) + (1 << (n - 1 - idx)) if (nxt := val | nums[idx]) == m else dfs(idx + 1, val) + dfs(idx + 1, nxt)
        
        return dfs(0, 0)
```
```Java []
class Solution {
    private int m, n;
    private int[] vals;

    public int countMaxOrSubsets(int[] nums) {
        vals = nums;
        n = nums.length;
        m = 0;
        for(int num: nums)
            m |= num;
        return dfs(0, 0);
    }

    private int dfs(int idx, int val) {
        if(idx == n)
            return val == m ? 1 : 0;
        int notPick = dfs(idx + 1, val);
        int nVal = val | vals[idx];
        if(nVal == m)
            return (1 << (n - 1 - idx)) + notPick;
        return notPick + dfs(idx + 1, nVal);
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var countMaxOrSubsets = function(nums) {
    const n = nums.length
    let m = 0
    for(const num of nums)
        m |= num
    
    dfs = function(idx, val) {
        if(idx == n)
            return val == m ? 1 : 0
        const notPick = dfs(idx + 1, val), nVal = nums[idx] | val
        if(nVal == m)
            return (1 << (n - 1 - idx)) + notPick
        return notPick + dfs(idx + 1, nVal)
    }
    
    return dfs(0, 0)
};
```
```Go []
func countMaxOrSubsets(nums []int) int {
    n, m := len(nums), 0
    for _, num := range nums {
        m |= num
    }

    var dfs func(idx, val int) int
    dfs = func(idx, val int) int {
        if idx == n {
            if val == m {
                return 1
            }
            return 0
        }
        if nVal := val | nums[idx]; nVal == m {
            return dfs(idx + 1, val) + (1 << (n - 1 - idx))
        } else {
            return dfs(idx + 1, val) + dfs(idx + 1, nVal)
        }
    }

    return dfs(0, 0)
}
```