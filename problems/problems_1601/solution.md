# [Python/Java/JavaScript/Go] 从大到小枚举 or 二进制枚举 (状态压缩) or 回溯

> slug: pythonjavajavascriptgo-cong-da-dao-xiao-abkmr
> date: 2022-02-27
> tags: Go, Java, JavaScript, Python, Python3
> question: Maximum Number of Achievable Transfer Requests (maximum-number-of-achievable-transfer-requests)
> url: https://leetcode.cn/problems/maximum-number-of-achievable-transfer-requests/solutions/gPWMPl/pythonjavajavascriptgo-cong-da-dao-xiao-abkmr/

---
### 解题思路
从大到小枚举最多成立的请求数(记为$m$)，遍历这个请求数下，所有构成请求数的组合($C_n^m$个)中，有没有满足题目要求的，有的话直接返回答案即可。

二进制枚举requests被选取的情况，比如二进制最右边位如果是1，代表requests[0]被计入答案，用二进制形式枚举requests的所有组合，依次看是否可行更新最大答案。

回溯枚举每个请求被选择的情况，并用一个数组维护出入度差异，最终返回最大选的总数。

### 代码
从大到小枚举组合
```Python3
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        for i in range(len(requests), 0, -1):
            # 组合统计 m个requests里选取i个的所有组合
            for comb in combinations(requests, i):
                # 统计出度入度是否完全相等
                cnts = [0] * n
                for a, b in comb:
                    # 出度, 入度
                    cnts[a] += 1
                    cnts[b] -= 1
                if all(not c for c in cnts):
                    return i
        return 0
```
二进制枚举
```Java []
class Solution {
    public int maximumRequests(int n, int[][] requests) {
        int ans = 0, m = requests.length;
        out:
        for(int i = 1; i < 1 << m; i++) {
            int[] cnts = new int[n];
            int cur = 0;
            for(int j = 0; j < m; j++)
                if(((1 << j) & i) > 0) {
                    cnts[requests[j][0]]++;
                    cnts[requests[j][1]]--;
                    cur++;
                }
            for(int j = 0; j < n; j++)
                if(cnts[j] != 0) 
                    continue out;
            ans = Math.max(ans, cur);
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @param {number[][]} requests
 * @return {number}
 */
var maximumRequests = function(n, requests) {
    const m = requests.length
    let ans = 0
    for(let i = 1; i < 1 << m; i++) {
        const cnts = new Array(n).fill(0)
        let cur = 0, check = true
        for(let j = 0; j < m; j++) {
            if(((1 << j) & i) > 0) {
                cnts[requests[j][0]]++
                cnts[requests[j][1]]--
                cur++
            }
        }
        for(const c of cnts) {
            if(c != 0) {
                check = false
                break
            }
        }
        if(check)
            ans = Math.max(ans, cur)
    }
    return ans
};
```
```Go []
func maximumRequests(n int, requests [][]int) (ans int) {
    out:
    for i, m := 1, len(requests); i < 1 << m; i++ {
        cur, cnts := 0, make([]int, n)
        for j := 0; j < m; j++ {
            if (1 << j) & i > 0 {
                cnts[requests[j][0]]++
                cnts[requests[j][1]]--
                cur++
            }
        }
        for j := 0; j < n; j++ {
            if cnts[j] != 0 {
                continue out
            }
        }
        if cur > ans {
            ans = cur
        }
    }
    return
}
```
回溯
```Java []
class Solution {
    public int maximumRequests(int n, int[][] requests) {
        int[] cnts = new int[n];
        return backtrack(cnts, requests, 0, 0);
    }

    private int backtrack(int[] cnts, int[][] requests, int idx, int picked) {
        if(idx == requests.length)  {
            for(int c: cnts)
                if(c != 0)
                    return 0;
            return picked;
        }
        int ans = 0;
        cnts[requests[idx][0]]++;
        cnts[requests[idx][1]]--;
        ans = Math.max(ans, backtrack(cnts, requests, idx + 1, picked + 1));
        cnts[requests[idx][0]]--;
        cnts[requests[idx][1]]++;
        return Math.max(ans, Math.max(ans, backtrack(cnts, requests, idx + 1, picked)));
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @param {number[][]} requests
 * @return {number}
 */
var maximumRequests = function(n, requests) {
    const cnts = new Array(n).fill(0), m = requests.length
    dfs = function(i, picked) {
        if(i == m) {
            for(let j = 0; j < n; j++)
                if(cnts[j] != 0)
                    return 0
            return picked
        }
        cnts[requests[i][0]]++
        cnts[requests[i][1]]--
        const pMax = dfs(i + 1, picked + 1)
        cnts[requests[i][0]]--
        cnts[requests[i][1]]++
        return Math.max(pMax, dfs(i + 1, picked)) 
    }
    return dfs(0, 0)
};
```
```Go []
func maximumRequests(n int, requests [][]int) int {
    cnts, m := make([]int, n), len(requests)
    var dfs func(i, picked int) int
    dfs = func(i, picked int) int {
        if i == m {
            for _, c := range cnts {
                if c != 0 {
                    return 0
                }
            }
            return picked
        }
        cnts[requests[i][0]]++
        cnts[requests[i][1]]--
        pMax := dfs(i + 1, picked + 1)
        cnts[requests[i][0]]--
        cnts[requests[i][1]]++
        return max(pMax, dfs(i + 1, picked))
    }

    return dfs(0, 0)
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```