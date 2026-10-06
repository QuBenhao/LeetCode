# [Python] From straightforward 0/1 knapsack to backtracking (two pruning optimizations)

> Author: Benhao
> Date: 2021-06-18
> Upvotes: 23
> Tags: Python, Python3

---

### Approach
A string is a valid candidate if and only if it contains no duplicate characters. This also applies to strings formed by concatenation.
Maintain all valid concatenated strings found so far, consider every valid string that the current string can form, and return the maximum length.
<br>
The drawback is that **all concatenated strings must be retained throughout the process**. Solving the 0/1 knapsack problem with backtracking avoids this.
At position idx, the current concatenated string represents the 0/1 knapsack choices before idx. Explore all possible choices after it. After exploring the branch that includes an item, undo that inclusion and try later choices without it. Only after these branches have been searched do we backtrack to earlier knapsack choices and form new selections.
In other words, each branch has two subbranches: one includes i (the recursive dfs(i+1) call), and one excludes i (the loop iterations after i).
<br>
**Backtracking uses two pruning rules**
The first is `estimate the maximum possible answer initially and return as soon as the search reaches it`.
The other compares the current selection with the best answer: `if the current selection plus a heuristic upper bound for the remaining strings (allowing overlap with the current selection) cannot exceed the best answer, stop searching`. (Alternatively, `len(set(self.curr).union(*arr[idx:]))` gives a bound that excludes overlap with the current selection. In my tests, its performance and pruning seemed worse than the bound that allows overlap.)
<br>
- Points in the Python backtracking code that may need explanation:
    - The new arr contains sets representing valid strings.
    - The heuristic estimate ignores the selection constraints, allowing characters to be added whether or not they are already present.
    - Sets make it easy to check whether the intersection is empty.
    - For sets A,B: A.union(B) = A | B = $A \cup B$
    - For sets A,B: A & B = $A \cap B$, A & B is None $\iff A \cap B = \emptyset$
    - For sets A,B: A ^ B = $(A \cup B) \setminus (A \cap B)$. Since the intersection here is B, self.curr -= arr[i] can also undo the selection during backtracking.

### Code

```python3
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def validStr(string):
            return len(set(string)) == len(string)
        
        dp = []
        for s in arr:
            if not validStr(s):
                continue
            for s_ in list(dp):
                if validStr(s_ + s):
                    dp.append(s_ + s)
            dp.append(s)
        return len(max(dp,key=len)) if dp else 0

```

```python3
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Preprocess the data by removing strings with duplicate characters
        arr = [t for s in arr if len(t:=set(s)) == len(s)]
        # Estimate an upper bound on the result
        predict = len(set().union(*arr))
        n = len(arr)
        self.curr = set()
        self.ans = 0

        def dfs(idx):
            # Update the answer with the current selection's length
            self.ans = max(self.ans, len(self.curr))
            # Stop searching if the maximum possible result is reached, or if the current selection plus the remaining upper bound cannot improve the answer
            if self.ans == predict or idx == n or len(self.curr) + len(set().union(*arr[idx:])) < self.ans:
                return
            # Backtrack from idx to n to find the maximum 0/1 knapsack result
            for i in range(idx, n):
                # The current selection does not overlap with arr[idx]
                if not self.curr & arr[i]:
                    # Add to the selection, A+B
                    self.curr |= arr[i]
                    # Evaluate the maximum for the new selection
                    dfs(i+1)
                    # Backtrack and continue searching for the maximum, (A+B) - B
                    self.curr ^= arr[i]
        
        dfs(0)
        return self.ans
```
