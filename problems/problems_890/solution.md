# [Python/Java/TypeScript/Go] 模拟

> slug: -by-himymben-xdl2
> date: 2022-06-12
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Find and Replace Pattern (find-and-replace-pattern)
> url: https://leetcode.cn/problems/find-and-replace-pattern/solutions/xeAjjw/-by-himymben-xdl2/

---
### 解题思路
根据规则利用哈希表，遍历每个单词，逐个校验每个单词中的每个字母，查看是否存在满足题目的映射。

### 代码

```Python3 []
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(s: str) -> bool:
            ab, ba = dict(), dict()
            for w, p in zip(s, pattern):
                if w in ab or p in ba:
                    if ab.get(w, p) != p or ba.get(p, w) != w:
                        return False
                else:
                    ab[w] = p
                    ba[p] = w
            return True
        
        return [word for word in words if match(word)]
```
```Java []
class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        List<String> ans = new ArrayList<>();
        for (String word: words) {
            if (match(word, pattern)) {
                ans.add(word);
            }
        }
        return ans;
    }

    private boolean match(String word, String pattern) {
        HashMap<Character, Character> ab = new HashMap<>(), ba = new HashMap<>();
        for (int i = 0; i < word.length(); i++) {
            char w = word.charAt(i), p = pattern.charAt(i);
            if (ab.containsKey(w) || ba.containsKey(p)) {
                if ((ab.getOrDefault(w, p) != p) || (ba.getOrDefault(p, w) != w)) {
                    return false;
                }
            } else {
                ab.put(w, p);
                ba.put(p, w);
            }
        }
        return true;
    }
}
```
```TypeScript []
function findAndReplacePattern(words: string[], pattern: string): string[] {
    const match = (word: string): boolean => {
        const ab = new Map(), ba = new Map()
        for (let i = 0; i < word.length; i++) {
            const w = word.charCodeAt(i), p = pattern.charCodeAt(i)
            if (ab.has(w)) {
                if (ab.get(w) != p) {
                    return false
                }
            } else if (ba.has(p)) {
                if (ba.get(p) != w) {
                    return false
                }
            } else {
                ab.set(w, p)
                ba.set(p, w)
            }
        }
        return true
    }
    const ans = new Array()
    for(const word of words) {
        if (match(word)) {
            ans.push(word)
        }
    }
    return ans
};
```
```Go []
func findAndReplacePattern(words []string, pattern string) (ans []string) {
    match := func(word string) bool {
        ab, ba := map[byte]byte{}, map[byte]byte{}
        for i := 0; i < len(word); i++ {
            if v, ok := ab[word[i]]; ok {
                if v != pattern[i] {
                    return false
                }
            } else if vp, okp := ba[pattern[i]]; okp {
                if vp != word[i] {
                    return false
                }
            } else {
                ab[word[i]] = pattern[i]
                ba[pattern[i]] = word[i]
            }
        }
        return true
    }
    for _, word := range words {
        if match(word) {
            ans = append(ans, word)
        }
    }
    return
}
```