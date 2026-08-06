# [Python/Java/JavaScript/Go] 词频统计 + 子集判断

> slug: pythonjavajavascriptgo-ci-pin-tong-ji-zi-ozou
> date: 2021-12-10
> tags: Go, Java, JavaScript, Python, Python3
> question: Shortest Completing Word (shortest-completing-word)
> url: https://leetcode.cn/problems/shortest-completing-word/solutions/YJbmCa/pythonjavajavascriptgo-ci-pin-tong-ji-zi-ozou/

---
### 解题思路
用长度为26的数组记录'a'到'z'各自的个数，特别地将大写字母做相似的映射即可。

### 代码

```Python3 []
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def counter(word):
            cnts = [0] * 26
            for c in word:
                if 'a' <= c <= 'z':
                    cnts[ord(c) - ord('a')]+=1
                elif 'A' <= c <= 'Z':
                    cnts[ord(c) - ord('A')]+=1
            return cnts
        
        cs = counter(licensePlate)
        l, ans = inf, None
        for w in words:
            if len(w) < l:
                ws, i = counter(w), 0
                while i < len(cs):
                    if ws[i] < cs[i]:
                        break
                    i += 1
                if i == len(cs):
                    l, ans = len(w), w
        return ans
```
```Java []
class Solution {
    public String shortestCompletingWord(String licensePlate, String[] words) {
        int[] cnts = counter(licensePlate);
        int len = 1001;
        String ans = null;
        for(String word: words){
            if(word.length() < len){
                int[] ws = counter(word);
                int i = 0;
                for(;i<cnts.length && ws[i] >= cnts[i];i++){}
                if(i == cnts.length){
                    len = word.length();
                    ans = word;
                }
            }
        }
        return ans;
    }

    private int[] counter(String word) {
        int[] cnts = new int[26];
        for(int i=0;i<word.length();i++){
            char c = word.charAt(i);
            if(c <= 'z' && c >= 'a')
                cnts[c - 'a']++;
            else if(c <= 'Z' && c >= 'A')
                cnts[c - 'A']++;
        }
        return cnts;
    }
}
```
```JavaScript []
/**
 * @param {string} licensePlate
 * @param {string[]} words
 * @return {string}
 */
const a = 'a'.charCodeAt(), z = 'z'.charCodeAt(), A = 'A'.charCodeAt(), Z = 'Z'.charCodeAt()
var shortestCompletingWord = function(licensePlate, words) {
    counter = function(word) {
        const cnts = new Array(26)
        cnts.fill(0)
        for(let i=0;i<word.length;i++){
            const c = word.charCodeAt(i);
            if(c >= a && c <= z)
                cnts[c - a]++
            else if(c >= A && c <= Z){
                cnts[c - A]++
            }
        }
        return cnts
    }

    const cnts = counter(licensePlate)
    let ans
    for(const word of words)
        if(ans == undefined || word.length < ans.length){
            const ws = counter(word)
            let i = 0
            for(;i<cnts.length && ws[i] >= cnts[i];i++){}
            if(i == cnts.length)
                ans = word
        }
    return ans
};
```
```Go []
func shortestCompletingWord(licensePlate string, words []string) string {
    counter := func(word string) []int {
        cnts := make([]int, 26)
        for i := range word {
            if v := word[i]; v >= 'a' && v <= 'z' {
                cnts[v - 'a']++
            } else if v >= 'A' && v <= 'Z' {
                cnts[v - 'A']++
            }
        }
        return cnts
    }
    cnts := counter(licensePlate)
    l := 1001
    var ans string
    for _, word := range words {
        if len(word) < l {
            ws, i := counter(word), 0
            for ;i < len(cnts) && ws[i] >= cnts[i];i++ {}
            if i == len(cnts) {
                l, ans = len(word), word 
            }
        }
    }
    return ans
}
```