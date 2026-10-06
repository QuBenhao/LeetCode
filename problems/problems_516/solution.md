# [Python/Java/Go] Memoized recursion (99%) or interval DP

> Author: Benhao
> Date: 2021-08-12
> Upvotes: 20
> Tags: Go, Java, Python, Python3

---

### Approach
The recursive idea is somewhat greedy: for a character to form both ends of the longest palindromic subsequence, choose its leftmost and rightmost occurrences.
For example, in "bbbabc", if "b" forms both ends of the final palindrome, choose the first and last "b". Any other pair encloses a smaller substring, which is already covered by this greedy choice. The longest palindromic subsequence inside these two occurrences, together with the two "b" characters, gives the answer for this pair. That leads to recursion.

With this idea, the recursive code is straightforward:
```Python3
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        ans = 0
        for i,c in enumerate(s):
            # Find the rightmost occurrence of each character
            r = str.rindex(s, c)
            # If this is not the rightmost occurrence, recurse on the interior
            if r > i:
                ans = max(ans, self.longestPalindromeSubseq(s[i+1:r]) + 2)
            else:
                ans = max(ans, 1)
        return ans
```
Unsurprisingly, this exceeded the time limit.
Each call slices the string and searches for the rightmost occurrence. It also does not skip characters already considered: greedily pairing with the leftmost occurrence means the intermediate occurrences need not be tried.
We can fix this with memoization, using endpoint indices instead of slicing, and preprocessing the indices of every character so we can use binary search.

<br>
It is also worth describing the usual dynamic programming approach for palindromes. Equal characters at the two endpoints use one recurrence; unequal characters use another.
The idea is similar to the memoized recursion above. If the endpoint characters match, use the previously computed result: `dp[i][j] = dp[i+1][j-1] + 2`. Otherwise, take the larger result obtained by omitting either endpoint: `dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])`.

In this recurrence, the left endpoint i depends on i+1, and the right endpoint j depends on j-1, so iterate with i-- and j++.

### Code

```python3
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        n = len(s)
        # Preprocess all indices for each character
        cIndex = defaultdict(list)
        for i, c in enumerate(s):
            cIndex[ord(c) - ord('a')].append(i)
        
        @lru_cache(None)
        def dfs(l, r):
            if l >= r:
                return 1 if l == r else 0
            ans = 0
            # Find the leftmost and rightmost occurrences of a,b,c,d...,z in the interval l,r
            for i in range(26):
                left = bisect.bisect_left(cIndex[i], l)
                # This character does not occur in the interval
                if left == len(cIndex[i]):
                    continue
                right = bisect.bisect_left(cIndex[i], r)
                if right == len(cIndex[i]) or cIndex[i][right] > r:
                    right -= 1
                ans = max(ans, dfs(cIndex[i][left]+1, cIndex[i][right]-1) + 2) if right > left else max(ans, 1)
            return ans
        
        return dfs(0, n-1)
```
The same idea, just for fun~
```Python3
class Solution:
    @lru_cache(None)
    def longestPalindromeSubseq(self, s: str) -> int:
        return 0 if not s else max(self.longestPalindromeSubseq(s[l+1:r])+2 if (l:=s.index(c))<(r:=s.rindex(c)) else 1 for c in set(s))
```

```Go []
func longestPalindromeSubseq(s string) int {
    n := len(s)
    dp := make([][]int, n)
    for i := n - 1; i >= 0; i-- {
        dp[i] = make([]int, n)
        dp[i][i] = 1
        for j := i + 1; j < n; j++ {
            if s[i] == s[j] {
                dp[i][j] = dp[i + 1][j - 1] + 2
            } else {
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            }
        }
    }
    return dp[0][n - 1]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```
```Java []
class Solution {
    public int longestPalindromeSubseq(String s) {
        char[] chars = s.toCharArray();
        int n = chars.length;
        int[][] dp = new int[n][n];
        for(int i=n-1;i>=0;i--){
            dp[i][i] = 1;
            for(int j=i+1;j<n;j++){
                if(chars[i] == chars[j])
                    dp[i][j] = dp[i+1][j-1] + 2;
                else
                    dp[i][j] = Math.max(dp[i][j-1], dp[i+1][j]);
            }
        }
        return dp[0][n-1];
    }
}
```
