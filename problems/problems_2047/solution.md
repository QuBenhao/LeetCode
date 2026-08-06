# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-jx0s
> date: 2022-01-26
> tags: Go, Java, JavaScript, Python, Python3
> question: Number of Valid Words in a Sentence (number-of-valid-words-in-a-sentence)
> url: https://leetcode.cn/problems/number-of-valid-words-in-a-sentence/solutions/9E4OgP/pythonjavajavascriptgo-mo-ni-by-himymben-jx0s/

---
### 解题思路
基于题意判断按空格分割后的满足要求的单词个数。（PS：本题非常适合用DFA或正则匹配的思路解）

### 代码

```Python3 []
class Solution:
    def countValidWords(self, sentence: str) -> int:
        def helper(word):
            n, appear = len(word), False
            for i, c in enumerate(word):
                if 'a' <= c <= 'z':
                    continue
                elif c == '-':
                    if appear or not i or i == n - 1 or not ('a' <= word[i-1] <= 'z' and 'a' <= word[i+1] <= 'z'):
                        return False
                    appear = True
                elif c in '!.,':
                    if i != n - 1:
                        return False
                else:
                    return False
            return True
        
        return sum(helper(w) for w in sentence.split(' ') if w)
```
```Java []
class Solution {
    public int countValidWords(String sentence) {
        String[] words = sentence.split(" ");
        int ans = 0;
        for(String word: words)
            if(check(word))
                ans++;
        return ans;
    }

    private boolean check(String word){
        int n = word.length();
        if(n == 0)
            return false;
        boolean appear = false;
        for(int i = 0; i < n; i++){
            char c = word.charAt(i);
            if('a' <= c && c <= 'z')
                continue;
            else if(c == '-'){
                if(appear || i == 0 || i == n - 1)
                    return false;
                char cb = word.charAt(i-1), ca = word.charAt(i+1);
                if(!('a' <= cb && cb <= 'z' && 'a' <= ca && ca <= 'z'))
                    return false;
                appear = true;
            } else if(c == '!' || c == '.' || c == ',')
                return i == n - 1;
            else
                return false;
        }
        return true;
    }
}
```
```JavaScript []
/**
 * @param {string} sentence
 * @return {number}
 */
const A = 'a'.charCodeAt(0), Z = 'z'.charCodeAt(0), SP0 = '!'.charCodeAt(0), SP1 = '.'.charCodeAt(0), SP2 = ','.charCodeAt(0), SP = '-'.charCodeAt(0)
var countValidWords = function(sentence) {
    check = function(word) {
        const n = word.length
        if(n == 0)
            return false
        let appear = false
        for(let i = 0; i < n; i++){
            const c = word.charCodeAt(i)
            if(A <= c && c <= Z)
                continue
            else if(c == SP){
                if(appear || i == 0 || i == n - 1)
                    return false
                const cb = word.charCodeAt(i-1), ca = word.charCodeAt(i+1)
                if(!(A <= cb && cb <= Z && A <= ca && ca <= Z))
                    return false
                appear = true
            } else if(c == SP0 || c == SP1 || c == SP2)
                return i == n - 1
            else
                return false
        }
        return true
    }

    const words = sentence.split(" ")
    let ans = 0
    for(const word of words)
        if(check(word))
            ans++
    return ans
};
```
```Go []
func countValidWords(sentence string) (ans int) {
    for _, word := range strings.Split(sentence, " "){
        ans += check(word)
    }
    return
}

func check(word string) (ans int) {
    n := len(word)
    if n == 0 {
        return
    }
    appear := false
    for i := range word {
        b := word[i]
        if 'a' <= b && b <= 'z'{
            continue
        }else if b == '-'{
            if appear || i == 0 || i == n - 1 || !('a' <= word[i-1] && word[i-1] <= 'z' && 'a' <= word[i+1] && word[i+1] <= 'z'){
                return
            }
            appear = true
        } else if b == '!' || b == ',' || b == '.'{
            if i != n - 1 {
                return
            }
        } else {
            return
        }
    }
    ans++
    return
}
```

稍微学了下正则表达式，如果我理解的不对麻烦指出，感谢。
`[a-z]*` 匹配任意多的小写字母'a'到'z'
`([a-z]-[a-z]+)?` 有问号，整体可以不存在，也可以出现一次。以小写字母-小写字母出现
`[!.,]?$` 结尾可以为三种符号中的一种
```python3
class Solution:
    def countValidWords(self, sentence: str) -> int:
        return sum(bool(re.match(r'[a-z]*([a-z]-[a-z]+)?[!.,]?$', word)) for word in sentence.split(" ") if word)
```