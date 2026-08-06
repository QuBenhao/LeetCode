# [Python/Go/C] 模拟

> slug: pythongoc-mo-ni-by-himymben-m2f0
> date: 2024-02-28
> tags: C, Go, Java, Python3, TypeScript
> question: Reverse Words in a String (reverse-words-in-a-string)
> url: https://leetcode.cn/problems/reverse-words-in-a-string/solutions/cmIjJN/pythongoc-mo-ni-by-himymben-m2f0/

---

> Problem: [151. 反转字符串中的单词](https://leetcode.cn/problems/reverse-words-in-a-string/description/)

[TOC]

# 思路

> 去除多余的空格，按空格分割，将分割后的数组反转，最后空格拼接字符串

# 解题方法

> 模拟

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])
```
```Go []
func reverseWords(s string) string {
    ans := []byte{}
    for i := len(s) - 1; i >= 0; {
        word := []byte{}
        for i >= 0 && s[i] == ' ' {
            i--
        }
        for ; i >= 0 && s[i] != ' '; i-- {
            word = append(word, s[i])
        }
        for i >= 0 && s[i] == ' ' {
            i--
        }
        for j := len(word) - 1; j >= 0; j-- {
            ans = append(ans, word[j])
        }
        if i >= 0 {
            ans = append(ans, ' ')
        }
    }
    return string(ans)
}
```
```C []
void reverse(char *s, int left, int right) {
    for (int i = left, j = right; i < j; i++, j--) {
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;        
    }
}

void skipEmpty(char *s, int *idx) {
    while ((*idx) >= 0 && s[*idx] == ' ') {
        (*idx)--;
    }
}

char* reverseWords(char* s) {
    int n = strlen(s);
    char *ans = malloc(sizeof(char) * (n + 1));
    bzero(ans, sizeof(char) * (n + 1));
    for (int i = n - 1, idx = 0; i >= 0;) {
        skipEmpty(s, &i);
        int left = idx;
        while (i >= 0 && s[i] != ' ') {
            ans[idx++] = s[i--];
        }
        reverse(ans, left, idx - 1);
        skipEmpty(s, &i);
        if (i >= 0) {
            ans[idx++] = ' ';
        }
    }
    return ans;
}
```
