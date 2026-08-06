# [C] 模拟

> slug: c-mo-ni-by-himymben-uowz
> date: 2023-01-13
> tags: C, Go, Java, Python3, TypeScript
> question: Rearrange Characters to Make Target String (rearrange-characters-to-make-target-string)
> url: https://leetcode.cn/problems/rearrange-characters-to-make-target-string/solutions/YNgryk/c-mo-ni-by-himymben-uowz/

---
统计每一个字符的个数，s能覆盖target的多少倍，按木桶原理找最小

```C []
int min(int a, int b) {
    return a < b ? a : b;
}

int rearrangeCharacters(char * s, char * target){
    int tcnts[26], scnts[26];
    int i;
    for (i = 0; i < 26; i++) {
        tcnts[i] = 0;
        scnts[i] = 0;
    }
    for (i = 0; i < strlen(target); i++) {
        tcnts[target[i] - 'a']++;        
    }
    for (i = 0; i < strlen(s); i++) {
        scnts[s[i] - 'a']++;
    }
    int ans = strlen(s) / strlen(target);
    for (i = 0; i < 26; i++) {
        if (tcnts[i] != 0) {
            ans = min(ans, scnts[i] / tcnts[i]);
        }
    }
    return ans;
}
```
```Python3 []
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        return min(sc[k] // v for k, v in tc.items()) if (sc := Counter(s)) and (tc := Counter(target)) else 0
```