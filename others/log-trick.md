# log-trick

## gcd

记录最左侧gcd区间
```python3
from math import gcd

gs = []
for i, num in enumerate(nums):
    gs.append([[v, j] for v, j in gs[i - 1]] if i > 0 else [])
    g = gs[i]
    g.append([num, i])
    j = 0
    for p in g:
        p[0] = gcd(p[0], num)
        if g[j][0] != p[0]:
            j += 1
            g[j] = p
    del g[j + 1:]
```

记录最右侧gcd区间
```python3
from math import gcd


g = []
for i, x in enumerate(nums):
    g.append([x, i])

    j = 0
    for p in g:
        p[0] = gcd(p[0], x)
        if g[j][0] != p[0]:
            j += 1
            g[j] = p
        else:
            g[j][1] = p[1]
    del g[j + 1:]
```