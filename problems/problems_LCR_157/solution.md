# [Python] Take a shortcut with permutations (one line); remember both recursive and iterative approaches for interviews

> slug: python-permutations-by-qubenhao-3yqy
> date: 2021-06-21
> tags: Python, Python3
> question: 套餐内商品的排列顺序 (zi-fu-chuan-de-pai-lie-lcof)
> url: https://leetcode.cn/problems/zi-fu-chuan-de-pai-lie-lcof/solutions/jglzap/python-permutations-by-qubenhao-3yqy/

---
### Approach
permutations generates every permutation of a sequence but does not remove duplicates; use set for that.

**Recursion**
The recursive idea is simple: take each element from the list, place it first, and combine it with every permutation of the remaining elements. (There is substantial repeated work, so memoization reduced the time from 500ms to 100ms.)

**Iteration**
The iterative approach is more involved. Generate permutations in lexicographic order, from smallest to largest.
I remember a similar problem, perhaps from a weekly contest: for a number such as 19631, find the next permutation that is just larger than it. That operation solves this problem iteratively.
For example, 1234 is the smallest, followed by 1243, then 1324, and so on.

### Code

```python3
class Solution:
    def permutation(self, s: str) -> List[str]:
        return list(set(''.join(st) for st in itertools.permutations(s)))
```
Recursive solution
```python3
class Solution:
    @lru_cache(None)
    def permutation(self, s: str) -> List[str]:
        if len(s) <= 1:
            return [s]
        return list(set(s[i] + perm for i in range(len(s)) for perm in self.permutation(s[:i] + s[i+1:])))
```
Iterative solution
```python3
class Solution:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        curr = list(sorted(s))
        end = list(reversed(curr))
        ans = []
        # Generate the next permutation
        while curr != end:
            ans.append(''.join(curr))
            i = n - 2
            # 29631 -> 31269
            while i > 0 and curr[i] >= curr[i+1]:
                i -= 1
            j = n - 1
            while j > i-1 and curr[j] <= curr[i]:
                j -= 1
            curr[i], curr[j] = curr[j], curr[i]
            curr = curr[:i+1] + sorted(curr[i+1:])
        ans.append(''.join(end))
        return ans
```
