# [Python] sortedcontainers

> Author: Benhao
> Date: 2021-07-05
> Upvotes: 16
> Tags: Python, Python3

---

### 解题思路
统计所有的食物(桌)的排序，再统计每桌对应的食物有多少即可

不熟悉sortedcontainers的话，使用set然后sorted即可
`foods=set(), foods = sorted(foods)`

<br>
第一种方法性能不好是因为我们额外使用了Counter统计后返回结果，实际上我们可以直接在结果数组里统计数量最后变成str返回。

### 代码

```python3
from sortedcontainers import SortedSet


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = SortedSet()
        tables = defaultdict(Counter)
        for name,number,food in orders:
            foods.add(food)
            tables[number][food] += 1
        return [["Table"] + [food for food in foods]] + [[table] + [str(tables[table][food]) for food in foods] for table in sorted(tables.keys(), key=int)]
```

维护两个排序好的字典，对应idx
```python3
from sortedcontainers import SortedDict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # 转换orders为，所有订单里的全部桌和全部食物
        obj = list(zip(*orders))
        # 排序好的tables，每个table对应结果数组中的第几行
        tables = SortedDict({v:i for i,v in enumerate(sorted(map(int,set(obj[1]))), 1)})
        # 排序好的foods，每个food对应结果数组中的第几列
        foods = SortedDict({v:i for i,v in enumerate(sorted(set(obj[2])), 1)})
        # 生成结果数组并填好第一行第一列
        res = [["Table"] + [food for food in foods]] + [[str(key)] + ["0"] * len(foods) for key in tables]
        # 统计每桌每个食物的数量
        for _, table, food in orders:
            res[tables[int(table)]][foods[food]] = str(int(res[tables[int(table)]][foods[food]]) + 1)
        return res
```