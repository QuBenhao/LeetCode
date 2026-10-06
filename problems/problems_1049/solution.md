# [Python] Proving the reduction to a signed sum (mathematical induction)

> Author: Benhao
> Date: 2021-06-07
> Upvotes: 14
> Tags: Python, Python3

---

### Approach
Two stones $a$ and $b$ are the easiest case: the final result is either $a-b$ or $b-a$ (whichever is nonnegative, so we write $abs(a-b)$).

Suppose there are three stones, $a,b,c$, with $a \leq b \leq c$.
The three smashing orders are $(a,b),c$; $(a,c),b$; and $(b,c),a$.
Given their relative sizes, the three results are $a-b+c, abs(c-a-b), abs(c-b-a)$.

We only need the smallest of these results.

More generally, for $i$ stones, $s_1,s_2,..,s_i$, **the final result must be a sum formed by assigning a positive or negative sign to each stone (called a signed sum below)**.
(The examples above cover $i=2$ and $i=3$.)

Proof: assume the statement holds for $i$ stones, and show that it also holds for $i+1$ stones.
For stones $s_1,s_2,..,s_{i+1}$, choose any two to smash. Suppose they are $s_m$ and $s_n$; without loss of generality, let $sm \leq sn$.
The problem now has $i$ stones: $s_1, s_2, .., s_{m-1}, s_{m+1}, .., s_{n-1}, s_{n+1}, .. s_{i+1}, s_n-s_m$.
By the induction hypothesis, the answer for these $i$ stones is a signed sum of $s_1, s_2, ... , s_n-s_m$.
In the final result, the contribution from $s_1, s_2, .., s_{m-1}, s_{m+1}, .., s_{n-1}, s_{n+1}, .. s_{i+1}$ is already a signed sum of the original stones.
Now consider the final sign of $s_n-s_m$.
If $s_n-s_m$ is positive, this assigns a negative sign to stone $s_m$ and a positive sign to stone $s_n$; in the other case, $s_m$ is positive and $s_n$ is negative.
Thus, for any stones $s_m$ and $s_n$, $m,n \in 1,2,3,...,i+1$, the final result is a signed sum of the $i+1$ stones.

This completes the proof.

In other words, **the answer for n stones is always among their signed sums**.

With this proof, the original problem can be understood as splitting the stones into two groups with sums $positive$ and $negative$, minimizing the absolute difference $abs(positive - negative)$.

This explains why the problem can be reduced to a 0/1 knapsack problem.

Another day spent revising yesterday's code.

### Code

```python3
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx, curr):
            if idx == len(stones):
                return curr if curr >= 0 else inf
            return min(dfs(idx+1, curr+stones[idx]), dfs(idx+1, curr-stones[idx]))
        return dfs(0, 0)
```

```python3
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Greedy: find a subset sum as close as possible to sum//2
        @lru_cache(None)
        def dfs(idx, curr):
            if curr > t:
                return 0
            if idx == n:
                return curr
            return max(dfs(idx+1, curr + stones[idx]),dfs(idx+1, curr))
        
        n = len(stones)
        s = sum(stones)
        t = s // 2
        return s - 2 * dfs(0, 0)
```

```python3
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Greedy: find a subset sum as close as possible to sum//2
        s = sum(stones)
        t = s // 2
        sums = {0}

        for stone in stones:
            for cs in list(sums):
                if cs + stone < t:
                    sums.add(cs + stone)
                elif cs + stone == t:
                    return s - 2 * t
        return s - 2 * max(sums)
```
