# [Python] Sort by time, then run multi-source BFS within each time group

> Author: Benhao
> Date: 2021-11-28
> Upvotes: 8
> Tags: Python, Python3

---

### Approach
Maintain the set of people who know the secret throughout. At each time, intersect it with that time's meeting participants and use the intersection as BFS sources to spread the secret.

### Code

```python3
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        d = defaultdict(set)
        record = defaultdict(lambda:defaultdict(set))
        st = set()
        for x, y, t in meetings:
            d[t].add(x)
            d[t].add(y)
            record[t][x].add(y)
            record[t][y].add(x)
            st.add(t)
        knowns = {0, firstPerson}
        for t in sorted(st):
            queue = deque([k for k in knowns & d[t]])
            # print(t, d[t], record[t], queue)
            explored = set()
            while queue:
                k = queue.popleft()
                if k not in explored:
                    explored.add(k)
                    for other in record[t][k]:
                        if other not in explored:
                            queue.append(other)
                        knowns.add(other)
        return list(knowns)
```
