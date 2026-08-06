# [Python/Java/JavaScript/Go] 简单模拟

> slug: pythonjavajavascriptgo-jian-dan-mo-ni-by-l5hn
> date: 2022-04-20
> tags: Go, Java, JavaScript, Python, Python3
> question: Goat Latin (goat-latin)
> url: https://leetcode.cn/problems/goat-latin/solutions/kWhSl6/pythonjavajavascriptgo-jian-dan-mo-ni-by-l5hn/

---
### 解题思路
该用户太懒了只有代码

### 代码

```Python3 []
VOWELS = "aeiouAEIOU"
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        return " ".join((s if s[0] in VOWELS else s[1:] + s[0]) + "ma" + "a" * i for i, s in enumerate(sentence.split(" "), 1))
```
```Java []
class Solution {
    private static final Set<Character> VOWELS = new HashSet<>();
    static {
        VOWELS.add('a');
        VOWELS.add('e');
        VOWELS.add('i');
        VOWELS.add('o');
        VOWELS.add('u');
        VOWELS.add('A');
        VOWELS.add('E');
        VOWELS.add('I');
        VOWELS.add('O');
        VOWELS.add('U');
    } 
    public String toGoatLatin(String sentence) {
        StringBuilder sb = new StringBuilder();
        int n = sentence.length(), cnts = 1;
        for(int i = 0; i < n; i++) {
            char start = sentence.charAt(i++);
            if(VOWELS.contains(start))
                sb.append(start);
            while(i < n && sentence.charAt(i) != ' ')
                sb.append(sentence.charAt(i++));
            if(!VOWELS.contains(start))
                sb.append(start);
            sb.append("ma");
            for(int j = 0; j < cnts; j++)
                sb.append("a");
            if(i < n - 1)
                sb.append(" ");
            cnts++;
        }
        return sb.toString();
    }
}
```
```JavaScript []
const vowels = new Set();
vowels.add('a');
vowels.add('e');
vowels.add('i');
vowels.add('o');
vowels.add('u');
vowels.add('A');
vowels.add('E');
vowels.add('I');
vowels.add('O');
vowels.add('U');
/**
 * @param {string} sentence
 * @return {string}
 */
var toGoatLatin = function(sentence) {
    return sentence.split(" ").map((i, idx) => {
        const res = new Array()
        if(vowels.has(i.charAt(0))) {
            res.push(i)
        } else {
            res.push(i.substring(1))
            res.push(i.substring(0, 1))
        }
        res.push("ma")
        for(let j = 0; j <= idx; j++)
            res.push("a")
        return res.join("")
    }).join(" ")
};
```
```Go []
func toGoatLatin(sentence string) string {
    vowels := map[byte]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'A': true, 'E': true, 'I': true, 'O': true, 'U': true}
    ans := &strings.Builder{}
    for i, cnts, n := 0, 1, len(sentence); i < n; i++ {
        start := sentence[i]
        if vowels[start] {
            ans.WriteByte(start)
        }
        for i = i + 1; i < n && sentence[i] != ' '; i++ {
            ans.WriteByte(sentence[i])
        }
        if !vowels[start] {
            ans.WriteByte(start)
        }
        ans.WriteString("ma")
        ans.WriteString(strings.Repeat("a", cnts))
        cnts++
        if i < n - 1 {
            ans.WriteByte(' ')
        }
    }
    return ans.String()
}
```