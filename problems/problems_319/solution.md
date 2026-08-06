# [Python/Java/JavaScript/Go] 因子个数为奇数的数字是完全平方数

> slug: python-yin-zi-ge-shu-wei-qi-shu-de-shu-z-opqy
> date: 2021-11-14
> tags: Go, Java, JavaScript, Python, Python3
> question: Bulb Switcher (bulb-switcher)
> url: https://leetcode.cn/problems/bulb-switcher/solutions/bO3y5q/python-yin-zi-ge-shu-wei-qi-shu-de-shu-z-opqy/

---
### 解题思路
```Python3
# 1. 每次某个灯被开关，是当前遍历的i为它的因子
# 2. 某个灯被开关奇数次最后会亮着，偶数次最后会熄灭
# 3. 某个数的因子个数为奇数个，它的所有质因子都出现了偶数次（完全平方数）
# 小于等于n的完全平方数个数为，1^2 .. 2^2 .. ... sqrt(n) ^ 2,  即sqrt(n)
```

关于因子个数是奇数个，只能是完全平方数，也是老生常谈了。
计算因子个数可以用它的全部素因子出现的次数，用$(1+r_1) * (1+r_2) * \ldots * (1+r_k)$计算，这个是奇数只有所有质因子个数$r_i$全部为偶数，也就是完全平方数了
![20190812201920998.png](https://pic.leetcode.cn/1636930495-LOUJcM-20190812201920998.png)


### 代码

```Python3 []
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))
```
```Java []
class Solution {
    public int bulbSwitch(int n) {
        return (int)Math.sqrt(n);
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
var bulbSwitch = function(n) {
    return Math.floor(Math.sqrt(n));
};
```
```Go []
func bulbSwitch(n int) int {
    return int(math.Sqrt(float64(n)))
}
```