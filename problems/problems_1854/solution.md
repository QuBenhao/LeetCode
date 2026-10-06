# [Python] Simulation

> Author: Benhao
> Date: 2021-05-09
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Act as an impartial population counter: add 1 in each birth year and subtract 1 in each death year. Store yearly population changes in an array spanning 1950 through 2050.
Traverse from start to finish to count the people alive in each year.

### Code

```python3
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        people = [0] * 101
        base_year = 1950
        for b,d in logs:
            people[b-base_year] += 1
            people[d-base_year] -= 1
        curr = ans = m = 0
        for i,p in enumerate(people):
            curr += p
            if curr > m:
                m, ans = curr, base_year + i
        return ans
```
