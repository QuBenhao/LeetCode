# [Python] SortedDict

> Author: Benhao
> Date: 2021-07-09
> Upvotes: 7
> Tags: Python, Python3

---

### 解题思路
维护一个有序字典(字典套字典)，并使用二分查找来找到最大的timestamp的位置。

### 代码

```python3
from sortedcontainers import SortedDict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        keys = self.map[key].keys()
        idx = self.map[key].bisect_left(timestamp)
        if idx == len(keys) or keys[idx] > timestamp:
            idx -= 1
        return self.map[key][keys[idx]] if idx >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```