# [Python/Java/JavaScript/Go] Memoized recursion or iteration -> mathematics

> Author: Benhao
> Date: 2021-12-16
> Upvotes: 20
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
At each step, drink the bottles that can be exchanged, saving the remainder for later rounds.

An alternative mathematical derivation works backward:
```python3
# Every y empty bottles yield one empty bottle after exchanging and drinking
# Thus, each exchange consumes y-1 empty bottles
# However, y-1 bottles alone are not enough for an exchange
# Following this pattern:
# One exchange requires at least y bottles
# Two exchanges require at least y + y - 1 = 2 * y - 1 bottles
# Three exchanges require at least y + y - 1 + y - 1 = 3 * y - 2 bottles
# ...
# k exchanges require y + (k-1) * (y-1) = k * y - k + 1 bottles
# Solving for k: x = k * (y - 1) + 1  ===> k = (x-1)//(y-1)
# In other words, x bottles allow at most (x-1)//(y-1) exchanges
```

### Code

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

Mathematics
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
