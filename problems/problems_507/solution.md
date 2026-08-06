# [Python/Java/JavaScript/Go] 数学

> slug: pythonjavajavascriptgo-shu-xue-by-himymb-1ykq
> date: 2021-12-30
> tags: Go, Java, JavaScript, Python, Python3
> question: Perfect Number (perfect-number)
> url: https://leetcode.cn/problems/perfect-number/solutions/0b2hVU/pythonjavajavascriptgo-shu-xue-by-himymb-1ykq/

---
### 解题思路
完全参考[完全数](https://baike.baidu.com/item/完全数/370913?fr=aladdin)的性质。

最近的评论功能因为加审核制度所以总看不到，哎，和家人们断联的第四天。提前祝大家2022年新年快乐啦。

![IMG_2414.jpg](https://pic.leetcode.cn/1640903013-RJtvwh-IMG_2414.jpg)

刷力扣差不多正好一年有余，收获真的很多很多，给大家的小建议是不要浮躁，踏踏实实刷题最后一定会有收获。关键还认识了很多小伙伴儿！

明年继续加油！

### 代码

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

完美数: $2^{p - 1} * (2^{p} - 1)$ 且 $p$和$2^{p}-1$都为质数
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

其实上面这个性质在二进制中更明显，我们有$p$位$1$加上右边的$p-1$位$0$
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