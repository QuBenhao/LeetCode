# [Python/Java/JavaScript/Go] Enumerate sizes in descending order, bitmask enumeration, or backtracking

> slug: pythonjavajavascriptgo-cong-da-dao-xiao-abkmr
> date: 2022-02-27
> tags: Go, Java, JavaScript, Python, Python3
> question: Maximum Number of Achievable Transfer Requests (maximum-number-of-achievable-transfer-requests)
> url: https://leetcode.cn/problems/maximum-number-of-achievable-transfer-requests/solutions/gPWMPl/pythonjavajavascriptgo-cong-da-dao-xiao-abkmr/

---
### Approach
Enumerate the number of accepted requests, $m$, from largest to smallest. Check all $C_n^m$ combinations of that size, and return immediately when one satisfies the requirements.

Use a bitmask to indicate which requests are selected. For example, a 1 in the rightmost bit includes requests[0]. Enumerate every subset, check whether it is feasible, and update the maximum answer.

Use backtracking to choose whether to include each request. Maintain an array of differences between incoming and outgoing transfers, and return the maximum number selected.

### Code
Enumerate combinations by descending size
```Python3
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        for i in range(len(requests), 0, -1):
            # Enumerate all ways to choose i requests from m requests
            for comb in combinations(requests, i):
                # Check that all incoming and outgoing counts match
                cnts = [0] * n
                for a, b in comb:
                    # Outgoing count, incoming count
                    cnts[a] += 1
                    cnts[b] -= 1
                if all(not c for c in cnts):
                    return i
        return 0
```
Bitmask enumeration
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
Backtracking
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
