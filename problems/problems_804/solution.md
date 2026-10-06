# [Python/Java/JavaScript/Go] Brute force

> slug: pythonjavajavascriptgo-bao-li-by-himymbe-m0vo
> date: 2022-04-09
> tags: Go, Java, JavaScript, Python, Python3
> question: Unique Morse Code Words (unique-morse-code-words)
> url: https://leetcode.cn/problems/unique-morse-code-words/solutions/CNIVyK/pythonjavajavascriptgo-bao-li-by-himymbe-m0vo/

---
### Approach
Iterate over each word and its letters to build its code. Store distinct codes in a set and return the set's size.

### Code

```Python3 []
CODE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set("".join(CODE[ord(c) - ord('a')] for c in word) for word in words))
```
```Java []
class Solution {
    private static final String[] CODE = new String[]{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};

    public int uniqueMorseRepresentations(String[] words) {
        Set<String> ans = new HashSet<>();
        for(String word: words) {
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < word.length(); i++)
                sb.append(CODE[word.charAt(i) - 'a']);
            ans.add(sb.toString());
        }
        return ans.size();
    }
}
```
```JavaScript []
const CODE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    const ans = new Set()
    for(const word of words) {
        let sb = ''
        for(const c of word)
            sb += CODE[c.charCodeAt(0) - 'a'.charCodeAt(0)]
        ans.add(sb)
    }
    return ans.size
};
```
```Go []
func uniqueMorseRepresentations(words []string) int {
    code := []string{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}
    ans := map[string]bool{}
    for _, word := range words {
        sb := &strings.Builder{}
        for i := 0; i < len(word); i++ {
            sb.WriteString(code[word[i] - 'a'])
        }
        ans[sb.String()] = true
    }
    return len(ans)
}
```
