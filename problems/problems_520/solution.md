# [Python/Java/JavaScript/Go] 简单状态机 or 统计 or 倒序

> Author: Benhao
> Date: 2021-11-12
> Upvotes: 21
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
如果首字母是小写，那么整个单词必须是小写；
如果首字母是大写，第二个字母是小写，剩下的部分也必须小写；
否则必须全部大写

### 代码

```Python3 []
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if str.islower(word[0]):
            return str.islower(word)
        if len(word) <= 2:
            return True
        if str.islower(word[1]):
            return str.islower(word[2:])
        return str.isupper(word)
```
```Java []
class Solution {
    public boolean detectCapitalUse(String word) {
        char c = word.charAt(0);
        if(Character.isLowerCase(word.charAt(0))){
            for(int i=1;i<word.length();i++)
                if(!Character.isLowerCase(word.charAt(i)))
                    return false;
            return true;          
        }
        if(word.length() <= 2)
            return true;
        if(Character.isLowerCase(word.charAt(1))){
            for(int i=2;i<word.length();i++)
                if(!Character.isLowerCase(word.charAt(i)))
                    return false;
            return true;
        }
        for(int i=2;i<word.length();i++)
            if(Character.isLowerCase(word.charAt(i)))
                return false;
        return true;
    }
}
```
```JavaScript []
/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    if(islower(word.charAt(0))){
        for(const c of word){
            if(!islower(c))
                return false;
        }
        return true;
    }
    if(word.length <= 2)
        return true;
    if(islower(word.charAt(1))){
        for(let i=2;i<word.length;i++)
            if(!islower(word.charAt(i)))
                return false;
        return true;
    }
    for(let i=2;i<word.length;i++)
        if(islower(word.charAt(i)))
            return false;
    return true;
};

var islower = function(c) {
    return c >= 'a' && c <= 'z';
}
```
```Go []
func detectCapitalUse(word string) bool {
    allMatch := func(s string, l byte,r byte) bool {
        for i := range s {
            if s[i] < l || s[i] > r {
                return false
            }
        }
        return true
    }
    if allMatch(word[0:1], 'a', 'z') {
        return allMatch(word[1:], 'a', 'z')
    }
    if len(word) <= 2 {
        return true
    }
    if allMatch(word[1:2], 'a', 'z') {
        return allMatch(word[2:], 'a', 'z')
    }
    return allMatch(word[2:], 'A', 'Z')
}
```

另一种思路，统计大写的个数
```Python3 []
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return not (s:=sum(c.isupper() for c in word)) or (s == 1 and word[0].isupper()) or s == len(word)
```
```Go []
func detectCapitalUse(word string) bool {
    count := 0
    for _, r := range word {
        if r <= 'Z' && r >= 'A' {
            count++
        }
    }
    return count == 0 || count == len(word) || (count == 1 && word[0] <= 90 && word[0] >= 65)
}
```

倒序分别找最后一个大小写的坐标
```Python3 []
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        l = u = None
        for i in range(n-1,-1,-1):
            if word[i].islower() and l is None:
                l = i
            elif word[i].isupper() and u is None:
                u = i
            if l and u:
                break
        return l is None or not u
```
```Go []
func detectCapitalUse(word string) bool {
    lastLower, lastUpper := -1, -1
    // 也可以正序写，但是永远要完整遍历不会提前break
    for i, r := range word {
        if r <= 'z' && r >= 'a' {
            lastLower = i
        } else {
            lastUpper = i
        }
    }
    return lastLower == -1 || lastUpper == -1 || lastUpper == 0
}
```