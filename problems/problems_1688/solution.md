# [Python/Java/JavaScript/Go/C] Several ways to think about this problem

> Author: Benhao
> Date: 2022-01-24
> Upvotes: 20
> Tags: C, Go, Java, JavaScript, Python, Python3

---

### Approach
1. Recursion (mathematical induction)
> With one team, no match is needed.
> When $n = 1$, $f(1) = 0$.
> With more than one team, first play a match between any two teams. This leaves n-1 teams, so:
> For $n >= 2$, $f(n) = 1 + f(n - 1)$.
> This gives a recurrence, or we can derive an expression for f(n) by induction.
> $f(n) + f(n-1) + \ldots + f(1) = 1 + f(n-1) + 1 + f(n-2) + \ldots + 1 + f(1) + 0$
> Simplifying gives $f(n) = n - 1$.

2. Binary representation
> Each round divides by two, like a right shift in binary. Can we reason about the problem in binary?
> Powers of two avoid byes caused by an odd team count, so decompose the number into powers of two.
> (All numbers below are binary.)
> For example, 10110 becomes 10000 + 100 + 10.
> For a power of two, repeatedly shift right until reaching 1: 10000 teams need 1111 matches, 100 teams need 11 matches, and 10 teams need 1 match.
> The total is 1111 + 11 + 1, plus the matches needed for the remaining teams (the number of 1 bits in n).
> Apply an extra 1 to the original leftmost binary component first, turning 1111 into 10000.

### Code

```Python3 []
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1
```
```Java []
class Solution {
    public int numberOfMatches(int n) {
        return --n;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
var numberOfMatches = function(n) {
    return --n
};
```
```Go []
func numberOfMatches(n int) int {
    return n - 1
}
```
```C []
int numberOfMatches(int n){
    return n - 1;
}
```

Too easy? Try all the problems in 三叶姐姐's [wiki](https://github.com/SharingSource/LogicStack-LeetCode/wiki).
