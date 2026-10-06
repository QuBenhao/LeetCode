# [Python] Hash Counter

> slug: python-hash-counter-by-qubenhao-qp9t
> date: 2021-07-17
> tags: Python, Python3
> question: Group Anagrams LCCI (group-anagrams-lcci)
> url: https://leetcode.cn/problems/group-anagrams-lcci/solutions/YTrU0k/python-hash-counter-by-qubenhao-qp9t/

---
### Approach
Strings with identical letter counts but different orders have the same Counter. Convert the counts from 'a' to 'z' into a tuple to use as a dictionary key.
The sorted string can also serve as the hash key.
<br>
I would expect defaultdict to use a set as its value, since identical permutations should be deduplicated.
However, the test case ["",""] expects [["",""]], so keep the duplicates.

### Code

```python3
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hashCounter(s):
            cnts = [0] * 26
            for c in s:
                cnts[ord(c) - ord('a')] += 1
            return tuple(cnts)

        ans = defaultdict(list)
        for s in strs:
            ans[hashCounter(s)].append(s)
        return [v for v in ans.values()]
```

```python3
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            ans[''.join(sorted(s))].append(s)
        return list(ans.values())
```
