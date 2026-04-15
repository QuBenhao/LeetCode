# [Python/Java/JavaScript/Go] 记忆化递归 or 迭代 -> 数学

> Author: Benhao
> Date: 2021-12-16
> Upvotes: 20
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
每次先喝可以换酒的酒，不够换的攒着等后面几波再喝。

另一种数学反推思维
```python3
# 每y个空瓶子返回一个空瓶子
# 也就是每y个空瓶子消耗掉y-1个空瓶子
# 但是y-1本身不能换瓶子
# 以这个模式来看
# 换一次最少的瓶子要y个
# 换两次最少的瓶子要y + y - 1 = 2 * y - 1
# 换三次最少的瓶子要y + y - 1 + y - 1 = 3 * y - 2
# ...
# 换k次就需要 y + (k-1) * (y-1) = k * y - k + 1
# 反着算k的话，x = k * (y - 1) + 1  ===> k = (x-1)//(y-1)
# 换句话说，x瓶酒最多换 (x-1)//(y-1)次
```

### 代码

```Python3 []
class Solution:
    @lru_cache(None)
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return (d := numBottles // numExchange) * numExchange + self.numWaterBottles(d + numBottles % numExchange, numExchange) if numBottles >= numExchange else numBottles
```
```Java []
class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int ans = 0;
        while(numBottles >= numExchange){
            ans += numBottles - numBottles%numExchange;
            numBottles = numBottles/numExchange + numBottles%numExchange;
        }
        return ans + numBottles;
    }
}
```
```JavaScript []
/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var numWaterBottles = function(numBottles, numExchange) {
    let ans = 0
    while(numBottles >= numExchange){
        ans += numBottles - numBottles % numExchange
        numBottles = Math.floor(numBottles/numExchange) + numBottles % numExchange
    }
    return ans + numBottles
};
```
```Go []
func numWaterBottles(numBottles int, numExchange int)(ans int) {
    for numBottles >= numExchange {
        ans += numBottles - numBottles % numExchange
        numBottles = numBottles / numExchange + numBottles % numExchange
    }
    return ans + numBottles
}
```

数学
```Python3 []
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)
```
```Java []
class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        return numBottles + (numBottles - 1) / (numExchange - 1);
    }
}
```
```JavaScript []
/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var numWaterBottles = function(numBottles, numExchange) {
    return numBottles + Math.floor((numBottles - 1) / (numExchange - 1))
};
```
```Go []
func numWaterBottles(numBottles int, numExchange int)(ans int) {
    return numBottles + (numBottles - 1) / (numExchange - 1)
}
```