# [Python/Java/JavaScript/Go] Simple simulation

> slug: pythonjavajavascriptgo-jian-dan-mo-ni-by-kk3x
> date: 2021-11-29
> tags: Go, Java, JavaScript, Python, Python3
> question: Nth Digit (nth-digit)
> url: https://leetcode.cn/problems/nth-digit/solutions/RarZnB/pythonjavajavascriptgo-jian-dan-mo-ni-by-kk3x/

---
### Approach
First, observe the following pattern:
```python3
# 9 one-digit numbers ===> 1 * 9
# 90 two-digit numbers ===> 2 * 90
# 900 three-digit numbers ===> 3 * 900
# ...
```

To find the nth digit, determine the number's digit length, its position among numbers of that length, and the desired digit's position within it.
Remove the one-digit block (9 digits), then the two-digit block (180 digits), then the three-digit block (2700 digits), and so on.
If `n` is 200, the digit lies in a three-digit number at position $200-9-180=11$ in that block, or zero-based index $11-1=10$.
Each three-digit number contributes three digits, so the number's index is $\frac{10}{3}=3$, giving $103$. The desired digit is at position $10\%3=1$, which is $0$.

Also watch for overflow in Java and similar languages.

### Code

```python3 []
class Solution:
    def findNthDigit(self, n: int) -> int:
        cur, base = 1, 9
        while n > cur * base:
            n -= cur * base
            cur += 1
            base *= 10
        n -= 1
        # The number
        num = 10 ** (cur - 1) + n // cur
        # Digit position within the number
        idx = n % cur
        return num // (10 ** (cur - 1 - idx)) % 10
```
```Java []
class Solution {
    public int findNthDigit(int n) {
        int cur = 1, base = 9;
        while(n > cur * base){
            n -= cur * base;
            cur++;
            base*=10;
            if(Integer.MAX_VALUE / base < cur){
                break;
            }
        }
        n--;
        int num = (int)Math.pow(10,cur - 1) + n / cur, idx = n % cur;
        return num / (int)Math.pow(10,cur - 1 - idx) % 10;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
var findNthDigit = function(n) {
    let cur = 1, base = 9;
    while(n > cur * base){
        n -= cur * base;
        cur++;
        base*=10;
        if(Number.MAX_SAFE_INTEGER / base < cur){
            break;
        }
    }
    n--;
    const num = Math.pow(10,cur - 1) + Math.floor(n / cur), idx = n % cur;
    return Math.floor(num / Math.pow(10,cur - 1 - idx)) % 10;
};
```
```Go []
func findNthDigit(n int) int {
    cur, base, INT_MAX := 1, 9, int(^uint(0) >> 1)
    for n > cur * base {
        n -= cur * base
        cur++
        base *= 10
        if (INT_MAX / base < cur) {
            break
        }
    }
    n--
    num, idx := int(math.Pow10(cur - 1)) + n / cur, n % cur 
    return num / int(math.Pow10(cur - 1 - idx)) % 10
}
```
