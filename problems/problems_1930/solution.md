# [Python] Find matching characters on both sides

> Author: Benhao
> Date: 2021-07-11
> Upvotes: 8
> Tags: Python, Python3

---

### Approach
Between two occurrences of 'a', each distinct middle character can form an answer.
Record the previous index of 'a' and count intervening characters.
Count 'a' separately; if it occurs more than twice, add 1 to the answer.

Here, 'a' represents any character.

### Code

```python3
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = set()
        last_index = [-1] * 26
        count = [0] * 26 
        for i,c in enumerate(s):
            if 0 <= last_index[ord(c)-ord('a')] < i - 1:
                for c_ in set(s[last_index[ord(c)-ord('a')]+1:i]):
                    ans.add(c+c_+c)
            last_index[ord(c)-ord('a')] = i
            count[ord(c)-ord('a')] += 1
        return len(ans) + sum(i >= 3 for i in count)

```
