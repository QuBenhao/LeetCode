# [Python] Hash Counter

> slug: python-hash-counter-by-qubenhao-qp9t
> date: 2021-07-17
> tags: Python, Python3
> question: Group Anagrams LCCI (group-anagrams-lcci)
> url: https://leetcode.cn/problems/group-anagrams-lcci/solutions/YTrU0k/python-hash-counter-by-qubenhao-qp9t/

---
### 解题思路
字母个数相同排列不同实际上就是她们的Counter一致，Counter按'a'到'z'转换成tuple即可作为字典的hash值(key)。
同样可以使用排序后的字符串作为hash值。
<br>
按理说defaultdict应该使用set作为value，因为排列一致应该去掉啊。
但是["",""]的用例要的是[["",""]]，那就不去重复好了。。

### 代码

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