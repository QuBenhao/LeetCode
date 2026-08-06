# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-by-himymben-xx0m
> date: 2022-05-16
> tags: Go, Java, JavaScript, Python, Python3
> question: Verifying an Alien Dictionary (verifying-an-alien-dictionary)
> url: https://leetcode.cn/problems/verifying-an-alien-dictionary/solutions/67soMK/pythonjavajavascriptgo-by-himymben-xx0m/

---
### 解题思路
按order的规则逐位比较，从左往右只要有一组相邻单词不满足序，直接返回`false`即可。

### 代码

```Python3 []
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {c: i for i, c in enumerate(order)}
        for i, w in enumerate(words[:-1]):
            j = 0
            while j < len(w):
                if j == len(words[i + 1]) or (a := mp[w[j]] - mp[words[i + 1][j]]) > 0:
                    return False
                elif a < 0:
                    break
                j += 1
        return True
```
```Java []
class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < order.length(); i++) {
            map.put(order.charAt(i), i);
        }
        for(int i = 0; i < words.length - 1; i++) {
            for(int j = 0; j < words[i].length(); j++) {
                if(j == words[i + 1].length()) {
                    return false;
                }
                int a = map.get(words[i].charAt(j)), b = map.get(words[i + 1].charAt(j));
                if(a > b) {
                    return false;
                } else if(a < b) {
                    break;
                }
            }
        }
        return true;
    }
}
```
```JavaScript []
/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
var isAlienSorted = function(words, order) {
    const mp = new Map()
    for(let i = 0; i < order.length; i++) {
        mp.set(order.charAt(i), i)
    }
    for(const [i, w] of words.entries()) {
        if(i == words.length - 1) {
            break
        }
        for(let j = 0; j < w.length; j++) {
            if(j == words[i + 1].length) {
                return false
            }
            const a = mp.get(w.charAt(j)), b = mp.get(words[i + 1].charAt(j))
            if(a > b) {
                return false
            } else if(a < b) {
                break
            }
        }
    }
    return true
};
```
```Go []
func isAlienSorted(words []string, order string) bool {
    mp := map[byte]int{}
    for i := range order {
        mp[order[i]] = i
    }
    for i := 0; i < len(words) - 1; i++ {
        for j := 0; j < len(words[i]); j++ {
            if j == len(words[i + 1]) {
                return false
            }
            if diff := mp[words[i][j]] - mp[words[i + 1][j]]; diff > 0 {
                return false
            } else if diff < 0 {
                break
            }
        }
    }
    return true
}
```

一行版
```python3
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return sorted(words, key=lambda x:tuple(mp[c] for c in x)) == words if (mp := {c:i for i, c in enumerate(order)}) else False
```

更新一个itertools的pairwise用法 [@jerryluan](/u/jerryluan/)
```python3
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {c: i for i, c in enumerate(order)}
        for w1, w2 in pairwise(words):
            j = 0
            while j < len(w1):
                if j == len(w2) or (a := mp[w1[j]] - mp[w2[j]]) > 0:
                    return False
                elif a < 0:
                    break
                j += 1
        return True
```