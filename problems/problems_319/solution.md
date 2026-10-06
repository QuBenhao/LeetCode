# [Python/Java/JavaScript/Go] Numbers with an odd number of factors are perfect squares

> slug: python-yin-zi-ge-shu-wei-qi-shu-de-shu-z-opqy
> date: 2021-11-14
> tags: Go, Java, JavaScript, Python, Python3
> question: Bulb Switcher (bulb-switcher)
> url: https://leetcode.cn/problems/bulb-switcher/solutions/bO3y5q/python-yin-zi-ge-shu-wei-qi-shu-de-shu-z-opqy/

---
### Approach
```Python3
# 1. A bulb is toggled when the current i is a factor of its number
# 2. A bulb toggled an odd number of times ends on; an even number of times ends off
# 3. A number has an odd number of factors when every prime factor has an even exponent (a perfect square)
# The perfect squares at most n are 1^2, 2^2, ..., sqrt(n)^2, giving sqrt(n) such numbers
```

The fact that only perfect squares have an odd number of factors is well known.
Use the exponents of all prime factors to count divisors: $(1+r_1) * (1+r_2) * \ldots * (1+r_k)$. This product is odd only when every prime exponent $r_i$ is even, which means the number is a perfect square.
![20190812201920998.png](https://pic.leetcode.cn/1636930495-LOUJcM-20190812201920998.png)


### Code

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
