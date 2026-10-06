# [Python/Java/JavaScript/Go] A classic base-conversion insight

> slug: pythonjavajavascriptgo-hen-jing-dian-de-qilwu
> date: 2021-11-24
> tags: Go, Java, JavaScript, Python, Python3
> question: Poor Pigs (poor-pigs)
> url: https://leetcode.cn/problems/poor-pigs/solutions/G8HAk4/pythonjavajavascriptgo-hen-jing-dian-de-qilwu/

---
### Approach
```python3
# Classic puzzle: one of 1024 buckets is poisoned; how can ten mice identify it in one test?
# Write 0~1023 in binary using at most ten bits; each mouse drinks from all buckets with a 1 in its assigned bit
# The poisoned bucket's number has 1s at the positions of mice that died and 0s elsewhere
# Ten mice can distinguish 2^10 buckets in one round; what about two rounds?
# Two rounds correspond to base 3: each mouse can determine whether one digit is 0, 1, or 2
# Death in the first round means digit 1, death in the second means 2, and survival means 0
# From this perspective:
# x rounds correspond to base (x+1); the number of digits needed for buckets in that base gives the minimum number of mice
```

Thank you all for your continued company and encouragement! Let's keep going together. Happy Thanksgiving!

[See 三叶's solution for an explanation of maximizing information entropy this way](https://leetcode.cn/problems/poor-pigs/solution/gong-shui-san-xie-jin-zhi-cai-xiang-xian-69fl/)

### Code

```python3 []
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets, minutesToTest//minutesToDie + 1))
```
```Java []
class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        // Use the change-of-base formula here
        return (int)Math.ceil(Math.log(buckets)/Math.log(minutesToTest/minutesToDie + 1));
    }
}
```
```JavaScript []
/**
 * @param {number} buckets
 * @param {number} minutesToDie
 * @param {number} minutesToTest
 * @return {number}
 */
var poorPigs = function(buckets, minutesToDie, minutesToTest) {
    return Math.ceil(Math.log(buckets)/Math.log(Math.floor(minutesToTest/minutesToDie) + 1))
};
```
```Go []
func poorPigs(buckets int, minutesToDie int, minutesToTest int) int {
    return int(math.Ceil(math.Log(float64(buckets)) / math.Log(float64(minutesToTest/minutesToDie) + 1)))
}
```
