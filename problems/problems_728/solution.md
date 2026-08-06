# [Python/Java/JavaScript/Go] 暴力模拟

> slug: pythonjavajavascriptgoo-by-himymben-4n6f
> date: 2022-03-30
> tags: Go, Java, JavaScript, Python, Python3
> question: Self Dividing Numbers (self-dividing-numbers)
> url: https://leetcode.cn/problems/self-dividing-numbers/solutions/ZnGWUM/pythonjavajavascriptgoo-by-himymben-4n6f/

---
### 解题思路
早上起来看了眼题，想素数筛想睡着了😂因为讨论的因子总是在2-9之间，而质数只有2、3、5、7。
害，还是直接暴力吧先。

### 代码

```Python3 []
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check(x):
            b = x
            while x and (t := x % 10) and not b % t:
                x //= 10
            return not x
        return [num for num in range(left, right + 1) if check(num)]
```
```Java []
class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> ans = new ArrayList<>();
        for(int i = left; i <= right; i++)
            if(check(i))
                ans.add(i);
        return ans;
    }
    
    private boolean check(int num) {
        int x = num;
        while(x > 0) {
            int t = x % 10;
            if(t == 0 || num % t != 0)
                break;
            x /= 10;
        }
        return x == 0;
    }
}
```
```JavaScript []
/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    check = function(num) {
        let x = num
        while(x > 0) {
            const t = x % 10
            if(t == 0 || num % t != 0)
                break
            x = Math.floor(x / 10)
        }
        return x == 0
    }
    const ans = new Array()
    for(let i = left; i <= right; i++)
        if(check(i))
            ans.push(i)
    return ans
};
```
```Go []
func selfDividingNumbers(left int, right int) (ans []int) {
    check := func(num int) bool {
        for x := num; x > 0; x /= 10 {
            t := x % 10
            if t == 0 || num % t != 0 {
                return false
            }
        }
        return true
    }

    for i := left; i <= right; i++ {
        if check(i) {
            ans = append(ans, i)
        }
    }
    return
}
```