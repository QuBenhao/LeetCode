# [Python/Java/TypeScript/Go] 哈希计数暴力

> slug: -by-himymben-oe1t
> date: 2022-06-22
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Substring with Concatenation of All Words (substring-with-concatenation-of-all-words)
> url: https://leetcode.cn/problems/substring-with-concatenation-of-all-words/solutions/RXdMEs/-by-himymben-oe1t/

---
### 解题思路
枚举起始位置，按步长统计单词个数是否一致。

### 代码

```Python3 []
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        cnts, step = Counter(words), len(words[0])
        return [i for i in range(len(s) - step * len(words) + 1) if Counter([s[i+j*step:i+(j+1)*step] for j in range(len(words))]) == cnts]
```
```Java []
class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        Map<String, Integer> cnts = new HashMap<>();
        for (String word: words) {
            cnts.put(word, cnts.getOrDefault(word, 0) + 1);
        }
        List<Integer> ans = new ArrayList<>();
        out:
        for (int i = 0, step = words[0].length(), n = words.length; i <= s.length() - step * n; i++) {
            Map<String, Integer> cur = new HashMap<>(cnts);
            for (int j = 0; j < n; j++) {
                String subStr = s.substring(i + step * j, i + step * (j + 1));
                if (!cur.containsKey(subStr)) {
                    continue out;
                } else {
                    int v = cur.get(subStr);
                    if (--v == 0) {
                        cur.remove(subStr);
                    } else {
                        cur.put(subStr, v);
                    }
                }
            }
            ans.add(i);
        }
        return ans;
    }
}
```
```TypeScript []
function findSubstring(s: string, words: string[]): number[] {
    const cnts = new Map<string, number>(), ans = new Array<number>(), n = words.length, step = words[0].length
    for (const word of words) {
        if (cnts.has(word)) {
            cnts.set(word, cnts.get(word) + 1)
        } else {
            cnts.set(word, 1)
        }
    }
    out:
    for (let i = 0; i <= s.length - step * n; i++) {
        const curCnts = new Map<string, number>()
        for (let j = 0; j < n; j++) {
            const subStr = s.substr(i + j * step, step)
            if (!cnts.has(subStr)) {
                continue out
            }
            if (curCnts.has(subStr)) {
                curCnts.set(subStr, curCnts.get(subStr) + 1)
                if (curCnts.get(subStr) > cnts.get(subStr)) {
                    continue out
                }
            } else {
                curCnts.set(subStr, 1)
            }
        }
        ans.push(i)
    }
    return ans
};
```
```Go []
func findSubstring(s string, words []string) (ans []int) {
    cnts, step, n := map[string]int{}, len(words[0]), len(words)
    for _, word := range words {
        cnts[word]++
    }
    out:
    for i := 0; i <= len(s) - step * n; i++ {
        cur := map[string]int{}
        for j := 0; j < n; j++ {
            subStr := s[i + step * j : i + step * (j + 1)]
            if cnts[subStr] == 0 || cur[subStr] + 1 > cnts[subStr] {
                continue out
            }
            cur[subStr]++
        }
        ans = append(ans, i)
    }
    return
}
```