# [Python] 计数器

> Author: Benhao
> Date: 2021-06-13
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
可以分配只有每个出现字符的个数可以均分

### 代码

```python3
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter()
        for w in words:
            for c in w:
                counter[c] += 1
        return all(v % len(words) == 0 for v in counter.values())

```