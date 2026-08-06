# [C] 模拟

> slug: c-mo-ni-by-himymben-cegf
> date: 2023-01-26
> tags: C, Go, Java, Python3, TypeScript
> question: Greatest English Letter in Upper and Lower Case (greatest-english-letter-in-upper-and-lower-case)
> url: https://leetcode.cn/problems/greatest-english-letter-in-upper-and-lower-case/solutions/zrub3J/c-mo-ni-by-himymben-cegf/

---
```C []
char * greatestLetter(char * s){
    int check[26];
    int i, ans = -1;
    for (i = 0; i < 26; i++) {
        check[i] = 0;
    }
    for (i = 0; i < strlen(s); i++) {
        int cur = s[i] - 'A';
        if (cur < 26) {
            check[cur] |= 2;
        } else {
            check[cur - 32] |= 1;
        }
    }
    for (i = 0; i < 26; i++) {
        if ((check[i] & 3) == 3) {
            ans = i;
        }
    }
    if (ans == -1) {
        return "";
    }
    char *res = (char *)malloc(sizeof(char) * 2);
    res[0] = 'A' + ans;
    res[1] = '\0';
    return res;
}
```
```Python3 []
class Solution:
    def greatestLetter(self, s: str) -> str:
        return max(ans) if (ans := [c for c in string.ascii_uppercase if c in s and c.lower() in s]) else ""
```