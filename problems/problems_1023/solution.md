# [C/Py3/Java/Go/Ts] two pointer

> slug: cpy3javagots-two-pointer-by-himymben-lxmn
> date: 2023-04-14
> tags: C, Go, Java, Python3, TypeScript
> question: Camelcase Matching (camelcase-matching)
> url: https://leetcode.cn/problems/camelcase-matching/solutions/4ZaE5Z/cpy3javagots-two-pointer-by-himymben-lxmn/

---
> Problem: [1023. 驼峰式匹配](https://leetcode.cn/problems/camelcase-matching/description/)

[TOC]

# Code
```C []
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

bool match(char *src, char *pattern) {
    int i, j, m = strlen(src), n = strlen(pattern);
    for (i = 0, j = 0; i < m && j < n; i++) {
        if (src[i] == pattern[j]) {
            j++;
        } else if (src[i] >= 'A' && src[i] <= 'Z') {
            return false;
        }
    }
    while (i < m) {
        if (src[i] >= 'A' && src[i] <= 'Z') {
            return false;
        }
        i++;
    }
    return i == m && j == n;
}

bool* camelMatch(char ** queries, int queriesSize, char * pattern, int* returnSize){
    bool *ans = (bool *) malloc(sizeof(bool) * queriesSize);
    *returnSize = queriesSize;
    int i;
    for (i = 0; i < queriesSize; i++) {
        ans[i] = match(queries[i], pattern);
    }
    return ans;
}
```
```Python3 []
```
```Java []
```
```TypeScript []
```
```Go []
func camelMatch(queries []string, pattern string) (ans []bool) {
    for _, str := range(queries) {
        ans = append(ans, match(str, pattern))
    }
    return
}

func match(str, pattern string) bool {
    i, j, m, n := 0, 0, len(str), len(pattern)
    for ; i < m; i++ {
        if j < n && str[i] == pattern[j] {
            j++
        } else if str[i] >= 'A' && str[i] <= 'Z' {
            return false
        }
    }
    return j == n
}
```
