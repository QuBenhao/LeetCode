# 回文串

预处理方式

```go
package main

func handle(s string) [][]bool:
	n := len(s)
	isPalindrome := make([][]bool, n)
	for i := range isPalindrome {
		isPalindrome[i] = make([]bool, n)
		isPalindrome[i][i] = true
	}
	for i := n - 1; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			isPalindrome[i][j] = s[i] == s[j] && (i+2 >= j || isPalindrome[i+1][j-1])
		}
	}
    return isPalindrome
```
