# [Python/Java/TypeScript/Go] 拓扑

> slug: pythonjavatypescriptgo-by-himymben-xngf
> date: 2022-05-31
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: 火星词典 (Jf1JuT)
> url: https://leetcode.cn/problems/Jf1JuT/solutions/Nxkezb/pythonjavatypescriptgo-by-himymben-xngf/

---
### 解题思路
1. 遍历words统计所有出现的字母
2. 遍历words中相邻的每对儿，统计这两对儿字典序不同的原因（第一个出现不同的地方，如果都一样且前面的长，可以直接返回）
3. 从所有没有入度的字母开始，拓扑遍历所有转移（因为转移是满足字典序的，入度为0时加入的话，所有字典序比它小的都已经加入了，可以加入）

PS:
WA了三发才理解题意，
所有字母都要出现在最终的答案中，不是只有转移的。
别的就没啥了。

### 代码

```Python3 []
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph, s = defaultdict(list), set()
        for w in words:
            s = s.union(set(w))
        d = [0] * 26
        for a, b in pairwise(words):
            for ca, cb in zip(a, b):
                if ca != cb:
                    graph[ca].append(cb)
                    d[ord(cb) - ord('a')] += 1
                    break
            else: 
                if len(a) > len(b):
                    return ""
        start = [k for k in s if d[ord(k) - ord('a')] == 0]
        for ch in start:
            for nxt in graph[ch]:
                d[v := ord(nxt) - ord('a')] -= 1
                if not d[v]:
                    start.append(nxt)
        return "".join(start) if len(start) == len(s) else ""
```
```Java []
class Solution {
    public String alienOrder(String[] words) {
        Map<Character, List<Character>> graph = new HashMap<>();
        Set<Character> set = new HashSet<>();
        int[] d = new int[26];
        out:
        for(int i = 0; i < words.length; i++) {
            for(int j = 0; j < words[i].length(); j++) {
                set.add(words[i].charAt(j));
            }
            if(i < words.length - 1) {
                for(int j = 0; j < Math.min(words[i].length(), words[i + 1].length()); j++) {
                    char c1 = words[i].charAt(j), c2 = words[i + 1].charAt(j);
                    if(c1 != c2) {
                        List<Character> nxt = graph.getOrDefault(c1, new ArrayList<>());
                        nxt.add(c2);
                        graph.put(c1, nxt);
                        d[c2 - 'a']++;
                        continue out;
                    }
                }
                if(words[i].length() > words[i + 1].length()) {
                    return "";
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for(char c: set) {
            if(d[c - 'a'] == 0) {
                sb.append(c);
            }
        }
        for(int i = 0;i < sb.length(); i++) {
            char c = sb.charAt(i);
            if(graph.containsKey(c)) {
                for(char nxt: graph.get(c)) {
                    if(--d[nxt - 'a'] == 0) {
                        sb.append(nxt);
                    }
                }
            }
        }
        return sb.length() == set.size() ? sb.toString() : "";
    }
}
```
```TypeScript []
function alienOrder(words: string[]): string {
    const set = new Set<string>(), graph = new Map<string, Array<string>>(), d = new Array<number>(26).fill(0)
    out:
    for(let i = 0; i < words.length; i++) {
        for(let j = 0; j < words[i].length; j++) {
            set.add(words[i].charAt(j))
        }
        if(i < words.length - 1) {
            for(let j = 0; j < Math.min(words[i].length, words[i + 1].length); j++) {
                if(words[i].charCodeAt(j) != words[i + 1].charCodeAt(j)) {
                    if(graph.has(words[i].charAt(j))) {
                        graph.get(words[i].charAt(j)).push(words[i + 1].charAt(j))
                    } else {
                        graph.set(words[i].charAt(j), [words[i + 1].charAt(j)])
                    }
                    d[words[i + 1].charCodeAt(j) - 'a'.charCodeAt(0)]++
                    continue out
                }
            }
            if(words[i].length > words[i + 1].length) {
                return ""
            }
        }
    }
    const ans = new Array()
    for(const c of set) {
        if(d[c.charCodeAt(0) - 'a'.charCodeAt(0)] == 0) {
            ans.push(c)
        }
    }
    for(let i = 0; i < ans.length; i++) {
        const c = ans[i]
        if(graph.has(c)) {
            for(const nxt of graph.get(c)) {
                if(--d[nxt.charCodeAt(0) - 'a'.charCodeAt(0)] == 0) {
                    ans.push(nxt)
                }
            }
        }
    }
    return ans.length == set.size ? ans.join("") : "";
};
```
```Go []
func alienOrder(words []string) string {
    graph, set, d := map[byte][]byte{}, map[byte]bool{}, make([]int, 26)
    out:
    for i, word := range words {
        for j := range word {
            set[word[j]] = true
        }
        if i < len(words) - 1 {
            for j := 0; j < min(len(words[i]), len(words[i + 1])); j++ {
                if words[i][j] != words[i + 1][j] {
                    graph[words[i][j]] = append(graph[words[i][j]], words[i + 1][j])
                    d[words[i + 1][j] - 'a']++
                    continue out
                }
            } 
            if len(words[i]) > len(words[i + 1]) {
                return ""
            }
        }
    }
    ans := []byte{}
    for s := range set {
        if d[s - 'a'] == 0 {
            ans = append(ans, s)
        }
    }
    for i := 0; i < len(ans); i++ {
        for _, nxt := range graph[ans[i]] {
            d[nxt - 'a']--
            if d[nxt - 'a'] == 0 {
                ans = append(ans, nxt)
            }
        }
    }
    if len(ans) == len(set) {
        return string(ans)
    }
    return ""
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```