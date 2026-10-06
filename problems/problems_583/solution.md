# [Python/Java] A standard longest common subsequence (LCS) problem

> slug: pythonjava-lcs-zui-chang-gong-gong-zi-xu-la8y
> date: 2021-09-24
> tags: Java, Python, Python3
> question: Delete Operation for Two Strings (delete-operation-for-two-strings)
> url: https://leetcode.cn/problems/delete-operation-for-two-strings/solutions/LN3NLs/pythonjava-lcs-zui-chang-gong-gong-zi-xu-la8y/

---
### Approach
Finding the fewest deletions is equivalent to finding the longest common subsequence of the two strings: retaining the longest common subsequence requires the fewest deletions.

The longest common subsequence recurrence is:
If the characters match, $word1_i = word2_j$, the LCS ending at i and j extends the LCS without those characters: $dp[i][j] = dp[i-1][j-1] + 1$.
If the characters differ, omit one endpoint and take the longer LCS: $dp[i][j] = max(dp[i][j-1], dp[i-1][j])$.

Image from Introduction to Algorithms:
![image.png](https://pic.leetcode.cn/1632524761-VakGzA-image.png)


### Code

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
