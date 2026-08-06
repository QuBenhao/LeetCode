# [Python/Java/JavaScript/Go] 简单模拟

> slug: pythonjavajavascriptgo-jian-dan-mo-ni-by-kk3x
> date: 2021-11-29
> tags: Go, Java, JavaScript, Python, Python3
> question: Nth Digit (nth-digit)
> url: https://leetcode.cn/problems/nth-digit/solutions/RarZnB/pythonjavajavascriptgo-jian-dan-mo-ni-by-kk3x/

---
### 解题思路
首先我们很容易明白如下规律:
```python3
# 1位数 9个 ===> 1 * 9
# 2位数 90个 ===> 2 * 90
# 3位数 900个 ===> 3 * 900
# ...
```

我们要知道第n位是什么，其实就是要找它属于几位数，它在那位数里是第多少个数，以及最终要找是该位数的第几位。
我们依次排去一位数（9个），两位数（180个），三位数（2700个），
假如`n`是200，那么我们就知道它一定是三位数，且它是三位数里的第$200-9-180=11$位，转换成从0开始的坐标就是$11-1=10$，
三位数是每三位一个数，那么它就是三位数里的$\frac{10}{3}=3$，也就是$103$了。而我们要找该数里的$10\%3=1$位也就是$0$。

另外Java等语言中注意一下溢出处理。

### 代码

```python3 []
class Solution:
    def findNthDigit(self, n: int) -> int:
        cur, base = 1, 9
        while n > cur * base:
            n -= cur * base
            cur += 1
            base *= 10
        n -= 1
        # 数字
        num = 10 ** (cur - 1) + n // cur
        # 数字里的第几位
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