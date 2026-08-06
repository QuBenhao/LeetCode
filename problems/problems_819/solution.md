# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-mv7j
> date: 2022-04-16
> tags: Go, Java, JavaScript, Python, Python3
> question: Most Common Word (most-common-word)
> url: https://leetcode.cn/problems/most-common-word/solutions/iQkV98/pythonjavajavascriptgo-mo-ni-by-himymben-mv7j/

---
### 解题思路
段落换小写，按那些标点符号分割，统计非空字符串且不在禁用字符串中的数量最多的字符串。

### 代码

```Python3 []
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return max(Counter(re.split(r"[ ,.!?';]", paragraph.lower())).items(), key=lambda x:(len(x) > 0, x[0] not in b, x[1]))[0] if (b := set(banned + [""])) else ""
```
```Java []
class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Map<String, Integer> cnts = new HashMap<>();
        Set<String> banSet = new HashSet<>();
        for(String ban: banned)
            banSet.add(ban);
        String ls = paragraph.toLowerCase() + "#";
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < ls.length(); i++) {
            if(ls.charAt(i) >= 'a' && ls.charAt(i) <= 'z')
                sb.append(ls.charAt(i));
            else if(sb.length() > 0) {
                String cur = sb.toString();
                if(!banSet.contains(cur))
                    cnts.put(cur, cnts.getOrDefault(cur, 0) + 1);
                sb.delete(0, sb.length());
            }
        }
        String res = null;
        int max = 0;
        for(String key: cnts.keySet()) {
            if(cnts.get(key) > max) {
                max = cnts.get(key);
                res = key;
            }
        }
        return res;
    }
}
```
```JavaScript []
/**
 * @param {string} paragraph
 * @param {string[]} banned
 * @return {string}
 */
var mostCommonWord = function(paragraph, banned) {
    const cnts = new Map(), banSet = new Set()
    for(const ban of banned)
        banSet.add(ban)
    const ls = paragraph.toLowerCase() + "#"
    let strs = new Array()
    for(let i = 0; i < ls.length; i++) {
        const code = ls.charCodeAt(i)
        if('a'.charCodeAt(0) <= code && code <= 'z'.charCodeAt(0))
            strs.push(ls.charAt(i))
        else if(strs.length > 0) {
            const curStr = strs.join('')
            if(!banSet.has(curStr)) 
                if(cnts.has(curStr))
                    cnts.set(curStr, cnts.get(curStr) + 1)
                else
                    cnts.set(curStr, 1)
            strs = new Array()
        }
    }
    let res = undefined, max = 0
    for(const key of cnts.keys()) {
        if(cnts.get(key) > max) {
            max = cnts.get(key)
            res = key
        }
    }
    return res
};
```
```Go []
func mostCommonWord(paragraph string, banned []string) (ans string) {
    cnts, banSet := map[string]int{}, map[string]bool{}
    for _, ban := range banned {
        banSet[ban] = true
    }
    ls := strings.ToLower(paragraph) + "#"
    var sb []byte
    for i := 0; i < len(ls); i++ {
        if ls[i] >= 'a' && ls[i] <= 'z' {
            sb = append(sb, ls[i])
        } else if len(sb) > 0 {
            s := string(sb)
            if !banSet[s] {
                cnts[s] = cnts[s] + 1
            }
            sb = nil
        }
    }
    max := 0
    for k, v := range cnts {
        if v > max {
            ans, max = k, v
        }
    }
    return
}
```