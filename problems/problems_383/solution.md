# [Python/Java/JavaScript/Go]

> slug: pythonjavajavascriptgo-by-himymben-vueu
> date: 2024-03-01
> tags: C, Go, Java, Python3, TypeScript
> question: Ransom Note (ransom-note)
> url: https://leetcode.cn/problems/ransom-note/solutions/8b3nim/pythonjavajavascriptgo-by-himymben-vueu/

---
### Approach
Compare the two frequency Counters.

### Code

```Python3 []
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return len(cr := Counter(ransomNote)) <= len(cm := Counter(magazine)) and not cr - cm
```
```Python3 []
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return (r:=Counter(ransomNote)) & Counter(magazine) == r
```
