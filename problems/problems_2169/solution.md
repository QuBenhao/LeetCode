# [Python/Go] Euclidean algorithm

> Author: Benhao
> Date: 2022-02-13
> Upvotes: 1
> Tags: Go, Python, Python3

---

### Approach
When one number is much larger than the other, the smaller number must be subtracted repeatedly: the number of subtractions is the larger number divided by the smaller.
After those subtractions, the larger number becomes the remainder, and the previously smaller number becomes the larger one.

### Code

```Python3 []
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1:
            ans += num2 // num1
            num1, num2 = num2 % num1, num1
        return ans
```
```Go []
func countOperations(num1 int, num2 int) (ans int) {
    for num1 > 0 {
        ans += num2/num1
        num1, num2 = num2 % num1, num1
    }
    return
}
```
