# [Python/Java] LCS 最长公共子序列模板题 

> slug: pythonjava-lcs-zui-chang-gong-gong-zi-xu-la8y
> date: 2021-09-24
> tags: Java, Python, Python3
> question: Delete Operation for Two Strings (delete-operation-for-two-strings)
> url: https://leetcode.cn/problems/delete-operation-for-two-strings/solutions/LN3NLs/pythonjava-lcs-zui-chang-gong-gong-zi-xu-la8y/

---
### 解题思路
求最少的删除次数，其实就是求两个字符串能构成的最长的公共子序列(最长的公共子序列需要的删除步数最少)。

而最长公共子序列的递推为：
如果两个位置的字符相等,即$word1_i = word2_j$，当前到i和j结尾的最长公共子序列就由去掉这个字符的最长公共子序列长度构成，也就是$dp[i][j] = dp[i-1][j-1] + 1$
如果两个位置的字符不相等，那么必然由两者之一的某一个结尾的最长公共子序列的长度构成，也就是$dp[i][j] = max(dp[i][j-1], dp[i-1][j])$

图片摘自算法导论：
![image.png](https://pic.leetcode.cn/1632524761-VakGzA-image.png)


### 代码

```Python3 []
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return m + n - dp[m][n] * 2
```
```Java []
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m+1][n+1];
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
                if(word1.charAt(i) == word2.charAt(j))
                    dp[i+1][j+1] = dp[i][j] + 1;
                else
                    dp[i+1][j+1] = Math.max(dp[i][j+1], dp[i+1][j]);
        return m + n - dp[m][n] * 2;
    }
}
```