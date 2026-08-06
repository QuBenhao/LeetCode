# [Python] 自定义哈希算法

> slug: python-zi-ding-yi-ha-xi-suan-fa-by-himym-rebw
> date: 2021-08-22
> tags: Python, Python3
> question: Group Shifted Strings (group-shifted-strings)
> url: https://leetcode.cn/problems/group-shifted-strings/solutions/kYJJCr/python-zi-ding-yi-ha-xi-suan-fa-by-himym-rebw/

---
### 解题思路
能通过移位得到的必须满足每位之间差距相等

### 代码

```python3
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # 字符串之间可以移位得到必然是每一位距离差对应一致的时候
        def hashCounter(string):
            return tuple(((ord(string[i]) - ord(string[i-1])) % 26) for i in range(1 , len(string))) if len(string) > 1 else 0

        ans = defaultdict(list)
        for s in strings:
            ans[hashCounter(s)].append(s)
        return list(ans.values())
```