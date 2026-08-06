# [Python/Java/JavaScript/Go] 模拟(三种解法)

> slug: pythonjavajavascript-mo-ni-by-himymben-bsp4
> date: 2021-11-03
> tags: Go, Java, JavaScript, Python, Python3
> question: Valid Perfect Square (valid-perfect-square)
> url: https://leetcode.cn/problems/valid-perfect-square/solutions/97ejRb/pythonjavajavascript-mo-ni-by-himymben-bsp4/

---
```Python3 []
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return (s:=int(sqrt(num))) * s == num
```
```Java []
class Solution {
    public boolean isPerfectSquare(int num) {
        // 1 + 3 + 5 + ... + (2 * n - 1) = (2 * n - 1 + 1) * n = n * n
        for(int i=1;num>0;i+=2)
            num -= i;
        return num == 0;
    }
}
```
```JavaScript []
/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    let l = 1, r = num;
    while(l <= r){
        const mid = l + Math.floor((r - l) / 2);
        const divid = Math.floor(num/mid);
        // 可能因为向下取整而相等，需要额外判断。 比如 10//3 = 3并不代表3*3=10
        if(mid == divid){
            if(num % mid == 0)
                return true;
            l = mid + 1;
        // 这个时候必然有 mid * mid > num
        }else if(mid > divid)
            r = mid - 1;
        else
            l = mid + 1;
    }
    return false;
};
```
```Go []
func isPerfectSquare(num int) bool {
    for i := 1; num > 0; i += 2 {
        num -= i
    }
    return num == 0
}
```