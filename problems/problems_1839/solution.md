# [Python] A shortcut

> Author: Benhao
> Date: 2021-04-25
> Upvotes: 1
> Tags: Python

---

### Approach
Track encountered characters in a set until a character is smaller than its predecessor, then update the answer.

### Code

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
