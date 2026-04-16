# [Python] 偷了个懒

> Author: Benhao
> Date: 2021-04-25
> Upvotes: 1
> Tags: Python

---

### 解题思路
用集合统计经历过的元素，直到遇到前面的比后面的字母大的时候，更新答案

### 代码

```python3
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ans = count = 0
        check = {'a', 'e', 'i', 'o', 'u'}
        explored = set()
        word += 'a'
        for i,c in enumerate(word):
            if i and word[i-1] > c:
                if explored == check:
                    ans = max(ans, count)
                count = 1
                explored = set()
            else:
                count += 1
            explored.add(c)
        return ans
```