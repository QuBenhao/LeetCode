# [Python] Memoized DFS

> Author: Benhao
> Date: 2021-05-24
> Upvotes: 3
> Tags: Python, Python3

---

### Approach
Deriving the recurrence:
Later printing overwrites earlier printing. If the string begins and ends with 'a', printing 'a' across the whole interval, then overwriting the middle, has the same final effect as printing the two endpoints separately, but uses a different number of turns.
Thus, printing 'aba' takes the same number of turns as printing 'ab'.

If the endpoints differ, they must be printed separately. Treat this as splitting the original string into two strings; the key is choosing the right split.
When can a split save a printing turn? That brings us back to the recurrence above.

The split position k can also be optimized. An optimal split that saves turns occurs where the character at k matches the character at i or j.

### Code

Before optimization
```python3
class Solution:
    def strangePrinter(self, s: str) -> int:
        # Preprocess runs of identical characters as one character; for example, "aaabbb" and "ab" are equivalent
        building = [s[0]]
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                building.append(s[i])

        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
            # If the characters at j and i match, printing i through j takes as many turns as i through j-1 (or i+1 through j)
            if building[i] == building[j]:
                return dfs(i, j - 1)
            # The characters at i and j differ; find the optimal split
            return min(dfs(i,k) + dfs(k+1,j) for k in range(i,j))

        return dfs(0, len(building) - 1)

```

After optimization
```python3
        # Preprocess runs of identical characters as one character; for example, "aaabbb" and "ab" are equivalent
        building = [s[0]]
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                building.append(s[i])

        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
            # If the characters at j and i match, printing i through j takes as many turns as i through j-1 (or i+1 through j)
            if building[i] == building[j]:
                return dfs(i, j - 1)
            # The characters at i and j differ; find the optimal split
            return min(dfs(i, k) + dfs(k + 1, j) for k in range(i, j)
                           if building[k] == building[i] or building[k] == building[j])

        return dfs(0, len(building) - 1)
```
