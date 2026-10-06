# [Python3] Remove matching portions and check whether the remainder is contiguous

> Author: Benhao
> Date: 2021-04-03
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
For consecutive indices, their sum is (first + last) * count / 2.

### Code

```python3
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        if len(sentence1) > len(sentence2):
            s1,s2 = s2,s1
        l = set([i for i in range(len(s2))])
        i = -1
        for s in s1:
            try:
                i = s2.index(s, i+1)
                l.remove(i)
            except:
                return False
        return not l or sum(l) == (min(l) + (len(l) + min(l) - 1)) * len(l) // 2

```
