# [Python/Java/JavaScript/Go] Mathematics

> Author: Benhao
> Date: 2022-04-10
> Upvotes: 15
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
For an n-digit number, the first digit has 9 choices, excluding 0.
For each remaining digit, choose an unused digit; the number of choices decreases from 9.
When n is greater than 0, also include the case with leading 0, which corresponds to the answer for n-1 digits.

### Code

```Python3 []
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return 1 if not n else reduce(lambda x,y:x*y, [9] + [i for i in range(9, 10 - n, -1)]) + self.countNumbersWithUniqueDigits(n - 1)
```
```Java []
class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        if(n == 0)
            return 1;
        int ans = 9;
        for(int i = 9; i > 10 - n; i--)
            ans *= i;
        return ans + countNumbersWithUniqueDigits(n - 1);
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    if(n == 0)
        return 1
    let ans = 9
    for(let i = 9; i > 10 - n; i--)
        ans *= i
    return ans + countNumbersWithUniqueDigits(n - 1)
};
```
```Go []
func countNumbersWithUniqueDigits(n int) int {
    if n == 0 {
        return 1
    }
    ans := 9
    for i := 9; i > 10 - n; i-- {
        ans *= i
    }
    return ans + countNumbersWithUniqueDigits(n - 1)
}
```
