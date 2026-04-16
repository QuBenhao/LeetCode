# [Python/Java] 模拟

> Author: Benhao
> Date: 2021-08-08
> Upvotes: 1
> Tags: Java, Python, Python3

---

### 解题思路
从头开始拼，能拼出s才行（复杂度比较高，不如找到和s等长的位置比较一次）

### 代码

```python3
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        return any(''.join(words[:i+1]) == s for i in range(len(words)))
```
优化后
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