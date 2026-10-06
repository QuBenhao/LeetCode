# [Python/Java] Simulation

> Author: Benhao
> Date: 2021-08-08
> Upvotes: 1
> Tags: Java, Python, Python3

---

### Approach
Concatenate from the beginning until s is formed. This is relatively expensive; comparing once when the length reaches len(s) is better.

### Code

```python3
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        return any(''.join(words[:i+1]) == s for i in range(len(words)))
```
Optimized version
```Python3 []
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        n = len(s)
        cur = ""
        for word in words:
            if len(cur) < n:
                cur += word
            else:
                break
        return s == cur
```
```Java []
class Solution {
    public boolean isPrefixString(String s, String[] words) {
        int n = s.length();
        StringBuilder sb = new StringBuilder();
        for(String word:words){
            if(sb.length() < n)
                sb.append(word);
            else
                break;
        }
        return s.compareTo(sb.toString()) == 0;
    }
}
```
