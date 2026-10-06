# [Python/Java/JavaScript/Go] Count poison duration before each refresh

> slug: pythonjavajavascriptgo-tong-ji-mei-ci-zh-h5h9
> date: 2021-11-09
> tags: Go, Java, JavaScript, Python, Python3
> question: Teemo Attacking (teemo-attacking)
> url: https://leetcode.cn/problems/teemo-attacking/solutions/6C7Sh7/pythonjavajavascriptgo-tong-ji-mei-ci-zh-h5h9/

---
### Approach
Use the next timestamp as the endpoint and check whether it refreshes the poison before the current effect ends.

### Code

```Python3 []
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        return sum(min(timeSeries[i+1], timeSeries[i] + duration) - timeSeries[i] for i in range(len(timeSeries) - 1)) + duration
```
```Java []
class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        int ans = duration;
        for(int i=0;i<timeSeries.length-1;i++)
            ans += Math.min(timeSeries[i+1], timeSeries[i] + duration) - timeSeries[i];
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
var findPoisonedDuration = function(timeSeries, duration) {
    let ans = duration;
    for(let i=0;i<timeSeries.length-1;i++)
        ans += Math.min(timeSeries[i+1], timeSeries[i] + duration) - timeSeries[i];
    return ans;
};
```
```Go []
func findPoisonedDuration(timeSeries []int, duration int) int {
    ans := duration
    for i := 0; i < len(timeSeries) - 1; i ++ {
        if timeSeries[i + 1] >= timeSeries[i] + duration {
            ans += duration
        } else {
            ans += timeSeries[i + 1] - timeSeries[i]
        }
    }
    return ans
}
```
