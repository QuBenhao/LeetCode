# KMP算法模板

```python
def kmp(s, pattern):
    # 构建next数组
    m = len(pattern)
    next_arr = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = next_arr[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        next_arr[i] = j

    # 匹配过程
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = next_arr[j - 1]
        if s[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1
```

```go
package main

func kmp(s, pattern string) int {
    m := len(pattern)
    next := make([]int, m)
    j := 0
    for i := 1; i < m; i++ {
        for j > 0 && pattern[i] != pattern[j] {
            j = next[j-1]
        }
        if pattern[i] == pattern[j] {
            j++
        }
        next[i] = j
    }
    
    j = 0
    for i := 0; i < len(s); i++ {
        for j > 0 && s[i] != pattern[j] {
            j = next[j-1]
        }
        if s[i] == pattern[j] {
            j++
        }
        if j == m {
            return i - m + 1
        }
    }
    return -1
}
```