# [Python/Java/JavaScript/Go] 找第k个空格的坐标

> Author: Benhao
> Date: 2021-12-05
> Upvotes: 18
> Tags: Go, Java, JavaScript, Python, Python3

---

```python3
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split(" ")[:k])
```

```Python3 []
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        idx = None
        for i, c in enumerate(s):
            if c == " ":
                k -= 1
            if not k:
                idx = i
                break
        return s[:idx] if idx is not None else s
```
```Java []
class Solution {
    public String truncateSentence(String s, int k) {
        int idx = -1;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)==' ')
                k--;
            if(k==0){
                idx = i;
                break;
            }
        }
        return idx == -1 ? s : s.substring(0, idx);
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var truncateSentence = function(s, k) {
    let idx = -1
    for(let i=0;i<s.length;i++){
        if(s.charAt(i)==' ')
            k--
        if(k==0){
            idx = i
            break
        }
    }
    return idx == -1 ? s : s.substr(0, idx)
};
```
```Go []
func truncateSentence(s string, k int) string {
    idx := -1
    for i := range s {
        if s[i] == ' ' {
            k--
        }
        if k == 0{
            idx = i
            break
        }
    }
    if idx == -1 {
        return s
    }
    return s[:idx]
}
```