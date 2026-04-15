# [Python/Java] 模拟

> Author: Benhao
> Date: 2021-09-22
> Upvotes: 1
> Tags: Java, Python, Python3

---

```Python3 []
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 3:
                return False
            n //= 3
        return True
```
```Java []
class Solution {
    public boolean isPowerOfThree(int n) {
        if(n <= 0)
            return false;
        for(;n>1;n/=3)
            if(n%3>0)
                return false;
        return true;
    }
}
```
```Python3 []
class Solution:
    def __init__(self):
        self.m = 1
        maxValue = (2 ** 31 - 1) // 3
        while self.m < maxValue:
            self.m *= 3

    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and self.m % n == 0
```
```Java []
class Solution {
    static int m = 1;
    static{
        while(m <= Integer.MAX_VALUE / 3)
            m *= 3;
    }
    public boolean isPowerOfThree(int n) {
        return n > 0 && m % n == 0;
    }
}
```