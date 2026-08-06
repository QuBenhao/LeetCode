# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-b39q
> date: 2022-02-02
> tags: Go, Java, JavaScript, Python, Python3
> question: Reverse Prefix of Word (reverse-prefix-of-word)
> url: https://leetcode.cn/problems/reverse-prefix-of-word/solutions/u7aZWj/pythonjavajavascriptgo-mo-ni-by-himymben-b39q/

---
```python3 []
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return word if (idx:=word.find(ch)) == -1 else word[:idx+1][::-1] + word[idx+1:]
```
```Java []
class Solution {
    public String reversePrefix(String word, char ch) {
        char[] cs = word.toCharArray();
        int i = 0;
        for(; i < cs.length; i++)
            if(cs[i] == ch)
                break;
        if(i == cs.length)
            return word;
        for(int l = 0; l < i; l++) {
            char tmp = cs[l];
            cs[l] = cs[i];
            cs[i--] = tmp;
        }
        return String.valueOf(cs);
    }
}
```
```JavaScript []
/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function(word, ch) {
    let i = 0
    while(i < word.length && word.charAt(i) != ch)
        i++
    return i == word.length ? word : word.substring(0, i + 1).split("").reverse().join("") + word.substring(i + 1)
};
```
```Go []
func reversePrefix(word string, ch byte) string {
    bt, i := []byte(word), 0
    for ; i < len(word) && word[i] != ch; i++ {}
    if i == len(word) {
        return word
    }
    for l := 0; l < i; l++ {
        bt[l], bt[i] = bt[i], bt[l]
        i--
    }
    return string(bt)
}
```