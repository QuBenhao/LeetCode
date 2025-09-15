# 回文串切割

```python
def min_cut(s):
    """
    :type s: str
    :rtype: int
    """

    n = len(s)

    is_palindrome = [[True for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            is_palindrome[j][i] = s[j] == s[i] and is_palindrome[j + 1][i - 1]

    dp = [i for i in range(n)]
    for i in range(n):
        if is_palindrome[0][i]:
            dp[i] = 0
        else:
            for j in range(1, i + 1):
                if is_palindrome[j][i]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)

    return dp[-1]

```

```go
package main

func minCut(s string) int {
	n := len(s)
	isPalindrome := make([][]bool, n)
	for i := 0; i < n; i++ {
		isPalindrome[i] = make([]bool, n)
	}
	for i := 0; i < n; i++ {
		for j := i; j >= 0; j-- {
			if s[j] == s[i] && (i-j <= 1 || isPalindrome[j+1][i-1]) {
				isPalindrome[j][i] = true
			}
		}
	}
	dp := make([]int, n)
	for i := 1; i < n; i++ {
		dp[i] = i
		if isPalindrome[0][i] {
			dp[i] = 0
		} else {
			for j := 1; j <= i; j++ {
				if isPalindrome[j][i] {
					dp[i] = min(dp[i], dp[j-1]+1)
				}
			}
		}
	}
	return dp[n-1]
}
```