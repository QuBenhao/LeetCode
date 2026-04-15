# [Python/Java/Go] 记忆化递归(99%) or 区间dp

> Author: Benhao
> Date: 2021-08-12
> Upvotes: 20
> Tags: Go, Java, Python, Python3

---

### 解题思路
有点儿贪心的递归思路，每个字母想要组成最大的回文子串的两端，那么它一定是取最左边和最右边的该字符的坐标。
比如说"bbbabc"，"b"如果是最终答案的回文串的两端，一定是第一个"b“和最后一个"b"，因为其他任意"b"的组合都比它更小(剩余字符串总是被最贪心的取法覆盖)。而以这两个"b"为两端，剩下的字符串中能取出多大的回文子序列，就构成了这两个"b"的答案，也就是递归的思想。

有了这个思路我们就很容易写出递归的代码:
```Python3
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        ans = 0
        for i,c in enumerate(s):
            # 每个字母找最右边的那个
            r = str.rindex(s, c)
            # 如果当前不是最右边的那个，往里面递归
            if r > i:
                ans = max(ans, self.longestPalindromeSubseq(s[i+1:r]) + 2)
            else:
                ans = max(ans, 1)
        return ans
```
然后不出意外的超时了。
每次都分割字符串、还要找最右的字母，还没有跳过被找过的字母(同样是贪心，要和最左边的那个字母组合，中间的其实不用尝试)。
问题不大，加个记忆化，不分割改成记录两端坐标，预处理所有的字母对应的所有坐标，这样就可以二分了。

<br>
还是提一下回文串常见的通用动态规划，当两个位置的字符相等，有一个递推，否则，有另一个递推。
和上面的记忆化递归思路大同小异，如果两边的字符相等，那么它由之前的计算结果得到`dp[i][j] = dp[i+1][j-1] + 2`;如果不相等，它由之前的不取某一边端点的最大值组成，也就是`dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])`。

由于我们的递推，左端点i依赖于i+1的结果，右端点j依赖于j-1的结果，所以采用i--,j++的递推方式。

### 代码

```python3
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        n = len(s)
        # 预处理统计每个字母的所有坐标
        cIndex = defaultdict(list)
        for i, c in enumerate(s):
            cIndex[ord(c) - ord('a')].append(i)
        
        @lru_cache(None)
        def dfs(l, r):
            if l >= r:
                return 1 if l == r else 0
            ans = 0
            # 找处于区间l,r最左最右的a,b,c,d...,z
            for i in range(26):
                left = bisect.bisect_left(cIndex[i], l)
                # 区间里没有这个字母
                if left == len(cIndex[i]):
                    continue
                right = bisect.bisect_left(cIndex[i], r)
                if right == len(cIndex[i]) or cIndex[i][right] > r:
                    right -= 1
                ans = max(ans, dfs(cIndex[i][left]+1, cIndex[i][right]-1) + 2) if right > left else max(ans, 1)
            return ans
        
        return dfs(0, n-1)
```
同款思路，就是玩儿~
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