# [Python/Java/JavaScript/Go] 统计每次中毒被刷新前的影响时长

> slug: pythonjavajavascriptgo-tong-ji-mei-ci-zh-h5h9
> date: 2021-11-09
> tags: Go, Java, JavaScript, Python, Python3
> question: Teemo Attacking (teemo-attacking)
> url: https://leetcode.cn/problems/teemo-attacking/solutions/6C7Sh7/pythonjavajavascriptgo-tong-ji-mei-ci-zh-h5h9/

---
### 解题思路
以下一个时间节点为终点，看当前影响的时长会不会被下一次刷新

### 代码

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