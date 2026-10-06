# [Python] Base 26

> Author: Benhao
> Date: 2021-06-28
> Upvotes: 11
> Tags: Python, Python3

---

### Approach
Essentially, we are writing a base-26 number with letters: A represents 1, B represents 2, ... Z represents 26.

Background
> To convert a decimal number $n$ to base k, repeatedly divide to calculate each digit, starting from the right.
We ultimately want to find $n = a_{0} * k^m + a_{1} * k^{m-1} + \ldots + a_{m} * 1$,
so $a_m = n$%$k$ (all preceding terms are multiplied by a power of k and are therefore divisible by k).
Then $(n - a_m) // k$ gives $a_0 * k^{m-1} + \ldots + a_{m-1} * 1$,
which lets us calculate $a_{m-1}$. Continue in the same way.
Another way to think about it: given a number, how would you extract each of its decimal digits?

**Approach 1**
This base-26 representation does not start at 0, so remap A to 0 and Z to 25, adding or subtracting 1 where needed to restore the original values.

**Approach 2**
If the addition and subtraction of 1 are hard to follow, use a direct mapping. In that mapping, A actually corresponds to Z, B to A, C to B, and so on.
The case representing Z, or 0, needs special care: it is not really 0 but a value of 26, so subtract that 26.

**Approach 3**
Finally, here is a recursive solution.

### Code

```python3
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        # Convert base 10 to base 26: A represents 1, B represents 2, ... Z represents 26
        while columnNumber > 0:
            # The rightmost digit is the result of the modulo operation
            columnNumber -= 1
            # A has ASCII code 65
            ans.append(chr(columnNumber%26 + 65))
            columnNumber //= 26
        return ''.join(ans[::-1])
```
```python3
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            curr = columnNumber%26
            # A remainder of 1 corresponds to A
            ans.append(chr(curr+64) if curr > 0 else 'Z')
            # If the division is exact, we still owe a value of 26
            columnNumber //= 26
            if not curr:
                columnNumber -= 1
        return ''.join(ans[::-1])
```
```python3
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        return self.convertToTitle((columnNumber-1)//26) + chr((columnNumber-1)%26 + 65) if columnNumber > 0 else ''
```
