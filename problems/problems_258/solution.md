# [Python/Java/JavaScript/Go] Mathematics

> slug: pythonjavajavascriptgo-shu-xue-by-himymb-9nkj
> date: 2022-03-02
> tags: Go, Java, JavaScript, Python, Python3
> question: Add Digits (add-digits)
> url: https://leetcode.cn/problems/add-digits/solutions/J6sgQd/pythonjavajavascriptgo-shu-xue-by-himymb-9nkj/

---
### Approach
Observations:
1. The final answer must be between 0 and 9.
2. Only 0 yields 0. Any other number has a nonzero digit, so its digit sum cannot become 0; its result must be between 1 and 9.
3. The function satisfies f(a + 1) = f(a) + 1 (treat a result of 10 as 1 here).

The results therefore cycle through 1-9 indefinitely.

The cycle length is 9, so f(a + 9) = f(a). Removing extra multiples of 9 leaves the result unchanged: f(a) = f(a % 9) (treat f(0) as 9 here).

### Code

```Python3 []
class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num else num
```
```Java []
class Solution {
    public int addDigits(int num) {
        return num == 0 ? num : (num - 1) % 9 + 1;
    }
}
```
```JavaScript []
/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    return num == 0 ? num : (num - 1) % 9 + 1
};
```
```Go []
func addDigits(num int) int {
    if num == 0 {
        return num
    } else {
        return (num - 1) % 9 + 1
    }
}
```
