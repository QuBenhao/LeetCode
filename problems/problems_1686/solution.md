# [Python] Greedy

> Author: Benhao
> Date: 2021-06-17
> Upvotes: 16
> Tags: Python, Python3

---

### Approach
Consider both players' valuations instead of simply taking your own highest value. Taking the highest combined value maximizes your score minus your opponent's score.

Suppose two stones have valuations $a_1, a_2$ and $b_1, b_2$.
The respective outcomes are $a_1 - b_2$ and $a_2 - b_1$.
Their difference is $a_1 - b_2 - a_2 + b_1 = (a_1 + b_1) - (a_2 + b_2)$.

Taking a stone also prevents the opponent from taking it. Since the opponent's score is subtracted from ours, denying that score acts like an addition.


### Code

```python3
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        totalValues = [(a+b) for a,b in zip(aliceValues, bobValues)]
        totalValues.sort(reverse=True)
        # Sum the combined values of Alice's stones, then subtract all of Bob's valuations to obtain the score difference
        ans = sum(totalValues[::2]) - sum(bobValues)
        if ans > 0:
            return 1
        elif ans < 0:
            return -1
        return 0
```
