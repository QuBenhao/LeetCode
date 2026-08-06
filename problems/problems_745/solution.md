# [Python/Java/TypeScript/Go] 哈希暴力

> slug: -by-himymben-eqe1
> date: 2022-07-14
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Prefix and Suffix Search (prefix-and-suffix-search)
> url: https://leetcode.cn/problems/prefix-and-suffix-search/solutions/Va47RU/-by-himymben-eqe1/

---
### 解题思路
记录每个单词的前缀后缀拼接组合，更新为最后一个坐标即可。

### 代码

```Python3 []
class WordFilter:

    def __init__(self, words: List[str]):
        self.map = {}
        for i, word in enumerate(words):
            for j in range(1, len(word) + 1):
                for k in range(1, len(word) + 1):
                    self.map[(word[:j], word[-k:])] = i

    def f(self, pref: str, suff: str) -> int:
        return self.map.get((pref, suff), -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
```
```Java []
class WordFilter {
    private Map<String, Integer> map;
    public WordFilter(String[] words) {
        map = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            for (int j = 1; j <= words[i].length(); j++) {
                for (int k = 1; k <= words[i].length(); k++) {
                    map.put(words[i].substring(0, j) + " " + words[i].substring(words[i].length() - k), i);
                }
            }
        }
    }
    
    public int f(String pref, String suff) {
        return map.getOrDefault(pref + " " + suff, -1);
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter obj = new WordFilter(words);
 * int param_1 = obj.f(pref,suff);
 */
```
```TypeScript []
class WordFilter {
    map: Map<string, number>
    constructor(words: string[]) {
        this.map = new Map<string, number>()
        for (const [i, word] of words.entries()) {
            for (let j = 1; j <= word.length; j++) {
                for (let k = 1; k <= word.length; k++) {
                    this.map.set(word.substring(0, j) + " " + word.substring(word.length - k), i)
                }
            }
        }
    }

    f(pref: string, suff: string): number {
        const key: string = pref + " " + suff
        return this.map.has(key) ? this.map.get(key) : -1
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * var obj = new WordFilter(words)
 * var param_1 = obj.f(pref,suff)
 */
```
```Go []
type WordFilter struct {
    Map map[string]int
}


func Constructor(words []string) WordFilter {
    mp := map[string]int{}
    for i, word := range words {
        for j, n := 1, len(word); j <= n; j++ {
            for k := 1; k <= n; k++ {
                mp[word[:j] + " " + word[n - k:]] = i
            }
        }
    }
    return WordFilter{mp}
}


func (this *WordFilter) F(pref string, suff string) int {
    if v, ok := this.Map[pref + " " + suff]; ok {
        return v
    } else {
        return -1
    }
}


/**
 * Your WordFilter object will be instantiated and called as such:
 * obj := Constructor(words);
 * param_1 := obj.F(pref,suff);
 */
```