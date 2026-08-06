# [Python/Go/C] 模拟

> slug: pythongoc-mo-ni-by-himymben-jq7t
> date: 2024-02-27
> tags: C, Go, Java, Python3, TypeScript
> question: Longest Common Prefix (longest-common-prefix)
> url: https://leetcode.cn/problems/longest-common-prefix/solutions/R6gQ9p/pythongoc-mo-ni-by-himymben-jq7t/

---

> Problem: [14. 最长公共前缀](https://leetcode.cn/problems/longest-common-prefix/description/)

[TOC]

# 思路

> 要么先遍历字符串数组再找最大交集，要么先遍历坐标判断是不是每个字符串该坐标都是同一个

# 解题方法

> 纵向+横向

# 复杂度

时间复杂度:
> $O(mn)$

空间复杂度:
> $O(mn)$



# Code
```Python3 []
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if strs:
            for i in range(200):
                cur = ""
                for j, s in enumerate(strs):
                    if len(s) < i + 1:
                        return ans
                    if not j:
                        cur = s[i]
                    elif s[i] != cur:
                        return ans
                else:
                    ans += cur
        return ans
```
```Go []
func longestCommonPrefix(strs []string) string {
    ans := []byte{}
    for i, n := 0, len(strs); i < 200; i++ {
        var cur byte
        for j := 0; j < n; j++ {
            if len(strs[j]) < i + 1 {
                return string(ans)
            }
            if j == 0 {
                cur = strs[j][i]
            } else if strs[j][i] != cur {
                return string(ans)
            }
        }
        ans = append(ans, cur)
    }
    return string(ans)
}
```
```C []
char* longestCommonPrefix(char** strs, int strsSize) {
    char *ans = malloc(sizeof(char) * 201);
    bzero(ans, sizeof(char) * 201);
    for (int i = 0, idx = 0; i < 200; i++) {
        char cur;
        for (int j = 0; j < strsSize; j++) {
            if (strlen(strs[j]) < i + 1) {
                goto end;
            }
            if (j == 0) {
                cur = strs[j][i];
            } else if (cur != strs[j][i]) {
                goto end;
            }
        }
        ans[idx++] = cur;
    }
    end:
    return ans;
}
```
  
