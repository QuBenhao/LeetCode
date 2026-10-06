# [Python/Java/JavaScript/Go] Mathematics

> slug: pythonjavajavascriptgo-shu-xue-by-himymb-1ykq
> date: 2021-12-30
> tags: Go, Java, JavaScript, Python, Python3
> question: Perfect Number (perfect-number)
> url: https://leetcode.cn/problems/perfect-number/solutions/0b2hVU/pythonjavajavascriptgo-shu-xue-by-himymb-1ykq/

---
### Approach
This relies entirely on the properties of [perfect numbers](https://baike.baidu.com/item/完全数/370913?fr=aladdin).

Comments have been hard to see lately because of the new moderation process. Sigh, this is the fourth day of losing touch with you all. Happy New Year 2022 in advance!

![IMG_2414.jpg](https://pic.leetcode.cn/1640903013-RJtvwh-IMG_2414.jpg)

I have been practicing on LeetCode for just over a year and have learned so much. My advice is to be patient and keep working steadily through problems; the effort will pay off. Best of all, I have met lots of friends!

Let's keep it up next year!

### Code

```python3 []
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in {6, 28, 496, 8128, 33550336, 8589869056}
```
```Java []
class Solution {
    private static final Set<Integer> set = new HashSet<>(){{
        add(6);
        add(28);
        add(496);
        add(8128);
        add(33550336);
    }};
    public boolean checkPerfectNumber(int num) {
        return set.contains(num);
    }
}
```
```JavaScript []
/**
 * @param {number} num
 * @return {boolean}
 */
const s = new Set()
s.add(6)
s.add(28)
s.add(496)
s.add(8128)
s.add(33550336)
var checkPerfectNumber = function(num) {
    return s.has(num)
};
```
```Go []
func checkPerfectNumber(num int) bool {
    return num == 6 || num == 28 || num == 496 || num == 8128 || num == 33550336
}
```

Perfect number: $2^{p - 1} * (2^{p} - 1)$, where both $p$ and $2^{p}-1$ are prime
```python3 []
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        def isPrime(x):
            for j in range(2, x//2):
                if not x % j:
                    return False
            return x > 1

        # 2^(p-1) * (2^p - 1)
        p = 1
        while not num % 2:
            num //= 2
            p += 1
        return num + 1 == pow(2, p) and isPrime(p) and isPrime(num)
```
```Java []
class Solution {
    public boolean checkPerfectNumber(int num) {
        int p = 1;
        while(num % 2 == 0){
            num >>= 1;
            p++;
        }
        return num + 1 == Math.pow(2, p) && isPrime(p) && isPrime(num);
    }

    private boolean isPrime(int num) {
        for(int j=2;j<num/2;j++)
            if(num % j == 0)
                return false;
        return num > 1;
    }
}
```
```JavaScript []
/**
 * @param {number} num
 * @return {boolean}
 */
var checkPerfectNumber = function(num) {
    isPrime = function(x) {
        for(let i=2;i<Math.floor(x/2);i++)
            if(x % i == 0)
                return false
        return x > 1
    }
    let p = 1
    while(num%2==0){
        num >>= 1
        p++
    }
    return num + 1 == 1 << p && isPrime(p) && isPrime(num)
};
```
```Go []
func checkPerfectNumber(num int) bool {
    p := 1
    for ; num % 2 == 0; p++{
        num >>= 1
    }
    return num + 1 == 1 << p && isPrime(p) && isPrime(num)
}

func isPrime(num int) bool {
    for i := 2; i < num / 2; i++ {
        if num % i == 0{
            return false
        }
    }
    return num > 1
}
```

This property is even clearer in binary: we have $p$ bits set to $1$, followed by $p-1$ bits set to $0$.
```python3
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        def isPrime(x):
            for j in range(2, x//2):
                if not x % j:
                    return False
            return x > 1

        # 2^(p-1) * (2^p - 1)
        return isPrime(p:=(len(bin(num))-1)//2) and isPrime(t:=(1 << p) - 1) and num == t << (p - 1)
```
