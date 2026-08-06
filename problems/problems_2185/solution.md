# [C] 模拟

> slug: c-mo-ni-by-himymben-gxme
> date: 2023-01-08
> tags: C, Go, Java, Python3, TypeScript
> question: Counting Words With a Given Prefix (counting-words-with-a-given-prefix)
> url: https://leetcode.cn/problems/counting-words-with-a-given-prefix/solutions/mhuaG6/c-mo-ni-by-himymben-gxme/

---
```C []
int prefixCount(char ** words, int wordsSize, char * pref) {
    int ans = 0, i, j;
    for (i = 0; i < wordsSize; i++) {
        if (strlen(words[i]) >= strlen(pref)) {
            for (j = 0; j < strlen(pref); j++) {
                if (words[i][j] != pref[j]) {
                    break;
                }
            }
            if (j == strlen(pref)) {
                ans++;
            }
        }
    }
    return ans;
}
```
```Python3 []
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(pref == word[:len(pref)] for word in words)
```
```Go []
func prefixCount(words []string, pref string) (ans int) {
    for _, word := range words {
        if strings.HasPrefix(word, pref) {
            ans++
        }
    }
    return
}
```