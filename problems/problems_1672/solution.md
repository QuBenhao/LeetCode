# [Python/Java/JavaScript/Go] 模拟

> Author: Benhao
> Date: 2022-04-13
> Upvotes: 17
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
该用户太懒了只有代码

### 代码

```Python3 []
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)
```
```Java []
class Solution {
    public int maximumWealth(int[][] accounts) {
        int ans = 0;
        for(int[] account: accounts) {
            int cur = 0;
            for(int val: account)
                cur += val;
            ans = Math.max(ans, cur);
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let ans = 0
    for(const account of accounts) {
        let cur = 0
        for(const val of account)
            cur += val
        ans = Math.max(ans, cur)
    }
    return ans
};
```
```Go []
func maximumWealth(accounts [][]int) (ans int) {
    for _, account := range accounts {
        cur := 0
        for _, val := range account {
            cur += val
        }
        if cur > ans {
            ans = cur
        }
    }
    return
}
```