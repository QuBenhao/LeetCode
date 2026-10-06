# [Python] Python's flexibility (100%) + enumerate the largest number of terms

> Author: Benhao
> Date: 2021-06-18
> Upvotes: 22
> Tags: Python, Python3

---

### Approach
Whatever the size of $n$, convert it to int first.

What does it mean for every digit of $n$ in base $x$ to be 1? It means $n = x^{m-1} + ... + x + 1$, so its base-$x$ representation is a string of $m$ ones: $\underbrace{11...1}_{m}$.
Enumerate from the largest number of terms $m$ to determine the smallest base x.
<br>

Suppose $n = x^{m-1} + x^{m-2} + ... + x + 1$, a sum of $m$ terms.
**How can we bound m?**
$n = x^{m-1} + x^{m-2} + ... + x + 1 > x^{m-1}$,
Therefore, $x^{m-1} < n$.
Smaller x permits larger m: a larger base requires fewer terms. Thus, the maximum $m$ occurs at base $x = 2$, which gives the largest possible number of terms.
Substituting into $2^{m-1} < n$ gives $m < \log_2n + 1$.
In code, use the binary length num.bit_length(), equivalent here to rounding log(num,2) up.
**How do we find x from m and n?**
Take the $(m-1)$th root of both sides of the inequality above:
$\sqrt[m-1]{x^{m-1}} < \sqrt[m-1]{n}$
That is, $x < \sqrt[m-1]{n}$.

Next, prove that $x+1 > \sqrt[m-1]{n}$:
The [binomial expansion](https://baike.baidu.com/item/二项展开式/7078006?fr=aladdin) shows that:
$(x+1)^{m-1} = x^{m-1} + a * x^{m-2} + ... + b * x + 1 > x^{m-1} + x^{m-2} + ... + x + 1 = n$. The exact coefficients do not matter; every power appears with a coefficient at least 1. Equality with n is impossible when m>2 because some intermediate coefficient exceeds 1.

Therefore:
$x < \sqrt[m-1]{n} < x + 1$
<br>

**A common way to simplify a geometric series is to multiply by the ratio and subtract to eliminate terms**:
We have $n * x = x^{m} + x^{m-1} + ... + x$.
Subtracting gives $n * x - n = x^{m} - 1$.
That is, n = $(x^{m} - 1)/(x-1)$.
<br>

If the loop finds no solution, $m = 2, x = n-1$ always provides one.
<br>
Replace 1/(m-1) with 1.0/(m-1) in Python to avoid integer floor division in Python 2.
### Code

```python3
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        # n = x^(m-1) + x^(m-2) + ... + x + 1
        for m in range(num.bit_length(),2,-1):
            # Binomial expansion: x^(m-1) < n < (x+1)^(m-1)
            x = int(pow(num,1/(m-1)))
            # Geometric series sum: n = (x^m - 1)/(x-1)
            if num == (pow(x,m) - 1)//(x-1):
                return str(x)
        return str(num-1)
```
