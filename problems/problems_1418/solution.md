# [Python] sortedcontainers

> Author: Benhao
> Date: 2021-07-05
> Upvotes: 16
> Tags: Python, Python3

---

### Approach
Sort all food names and table numbers, then count how many of each food each table ordered.

If sortedcontainers is unfamiliar, use set followed by sorted.
`foods=set(), foods = sorted(foods)`

<br>
The first method is slower because it uses an extra Counter before building the result. We can count directly in the result array, then convert the counts to str.

### Code

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

Maintain two sorted dictionaries mapping entries to idx.
```python3
from sortedcontainers import SortedDict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # Extract all tables and all foods from orders
        obj = list(zip(*orders))
        # Sorted tables: map each table to its row in the result array
        tables = SortedDict({v:i for i,v in enumerate(sorted(map(int,set(obj[1]))), 1)})
        # Sorted foods: map each food to its column in the result array
        foods = SortedDict({v:i for i,v in enumerate(sorted(set(obj[2])), 1)})
        # Create the result array and fill its first row and first column
        res = [["Table"] + [food for food in foods]] + [[str(key)] + ["0"] * len(foods) for key in tables]
        # Count each food ordered by each table
        for _, table, food in orders:
            res[tables[int(table)]][foods[food]] = str(int(res[tables[int(table)]][foods[food]]) + 1)
        return res
```
