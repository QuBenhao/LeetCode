# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-vwns
> date: 2022-01-30
> tags: Go, Java, JavaScript, Python, Python3
> question: Uncommon Words from Two Sentences (uncommon-words-from-two-sentences)
> url: https://leetcode.cn/problems/uncommon-words-from-two-sentences/solutions/Dh73t9/pythonjavajavascriptgo-mo-ni-by-himymben-vwns/

---
### 解题思路
按空格分割后统计单词频次，在一个里出现一次、在另一个里面没出现，换句话说就是在两个里面一共出现一次。

### 代码

```Python3 []
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [k for k, v in c.items() if v == 1] if (c := Counter(s1.split(" ")) + Counter(s2.split(" "))) else []
```
```Java []
class Solution {
    private Map<String, Integer> cnts;
    public String[] uncommonFromSentences(String s1, String s2) {
        cnts = new HashMap<>();
        count(s1);
        count(s2);
        List<String> ans = new ArrayList<>();
        cnts.forEach((k, v)->{
            if(v == 1)
                ans.add(k);
        });
        return ans.toArray(new String[ans.size()]);
    }

    private void count(String s){
        for(String sp: s.split(" ")){
            cnts.put(sp, cnts.getOrDefault(sp, 0) + 1);
        }
    }
}
```
```JavaScript []
/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
var uncommonFromSentences = function(s1, s2) {
    const cnts = new Map()
    const strs = (s1 + " " + s2).split(" ")
    strs.forEach(item=>{cnts.set(item, (cnts.get(item) || 0) + 1)})
    ans = new Array()
    for(const k of cnts.entries()){
        if(1 === k[1])
            ans.push(k[0])
    }
    return ans
};
```
```Go []
func uncommonFromSentences(s1 string, s2 string) (ans []string) {
    cnts := map[string]int{}
    strs1, strs2 := strings.Split(s1, " "), strings.Split(s2, " ")
    count(strs1, cnts)
    count(strs2, cnts)
    for k, v := range cnts {
        if v == 1 {
            ans = append(ans, k)
        }
    }
    return
}

func count(list []string, cnts map[string]int) {
    for _, s := range list {
        cnts[s] = cnts[s] + 1
    }
}
```