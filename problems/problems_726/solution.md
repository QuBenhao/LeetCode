# [Python] A single pass by working backward

> Author: Benhao
> Date: 2021-07-05
> Upvotes: 12
> Tags: Python, Python3

---

### Approach
Accumulate the multiplier inside parentheses while scanning backward. At an opening parenthesis, divide out the most recent factor to recover the multiplier for the following part of the reverse scan, which lies earlier in the original string.

### Code

```python3
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Scan backward while tracking the count map, total multiplier, multiplier stack, count, decimal place, and element name
        cnts, multiply, muls, num, num_count, atom = defaultdict(int), 1, [], 0, 0, ""
        for c in formula[::-1]:
            if c == ')':
                # If a number has been parsed, include it in the total multiplier
                if num:
                    multiply *= num
                    muls.append(num)
                    num = num_count = 0
                else:
                    muls.append(1)
            elif c == '(':
                # Remove the previous multiplier
                multiply //= muls.pop()
            elif str.isdigit(c):
                num += int(c) * (10 ** num_count)
                num_count += 1
            elif str.islower(c):
                atom += c
            else:
                atom += c
                # Always account for the total multiplier when updating an element's count
                if num:
                    cnts[atom[::-1]] += num * multiply
                else:
                    cnts[atom[::-1]] += multiply
                atom = ""
                num = num_count = 0
        return "".join(key if cnts[key] == 1 else key + str(cnts[key]) for key in sorted(cnts.keys()))
```
