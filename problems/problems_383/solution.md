# [Python/Java/JavaScript/Go]

> slug: pythonjavajavascriptgo-by-himymben-vueu
> date: 2024-03-01
> tags: C, Go, Java, Python3, TypeScript
> question: Ransom Note (ransom-note)
> url: https://leetcode.cn/problems/ransom-note/solutions/8b3nim/pythonjavajavascriptgo-by-himymben-vueu/

---
### 解题思路
比较两者的计数Counter即可

### 代码

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
