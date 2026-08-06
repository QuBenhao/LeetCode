# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-bc31
> date: 2022-01-09
> tags: Go, Java, JavaScript, Python, Python3
> question: Slowest Key (slowest-key)
> url: https://leetcode.cn/problems/slowest-key/solutions/3J6jOz/pythonjavajavascriptgo-mo-ni-by-himymben-bc31/

---
### 解题思路
遍历统计最大即可

### 代码

```Python3 []
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans, m = keysPressed[0], releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            if (diff := releaseTimes[i] - releaseTimes[i-1]) > m:
                ans, m = keysPressed[i], diff
            elif diff == m:
                ans = max(ans, keysPressed[i])
        return ans
```
```Java []
class Solution {
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        int ans = 0, m = releaseTimes[0];
        for(int i=1;i<releaseTimes.length;i++)
            if(releaseTimes[i] - releaseTimes[i-1] > m){
                m = releaseTimes[i] - releaseTimes[i-1];
                ans = i;
            } else if(releaseTimes[i] - releaseTimes[i-1] == m && keysPressed.charAt(i) > keysPressed.charAt(ans))
                ans = i;
        return keysPressed.charAt(ans);
    }
}
```
```JavaScript []
/**
 * @param {number[]} releaseTimes
 * @param {string} keysPressed
 * @return {character}
 */
var slowestKey = function(releaseTimes, keysPressed) {
    let ans = keysPressed[0], m = releaseTimes[0]
    for(let i=1;i<releaseTimes.length;i++)
        if(releaseTimes[i] - releaseTimes[i-1] > m){
            m = releaseTimes[i] - releaseTimes[i-1]
            ans = keysPressed[i]
        }else if(releaseTimes[i] - releaseTimes[i-1] == m && keysPressed[i] > ans)
            ans = keysPressed[i]
    return ans
};
```
```Go []
func slowestKey(releaseTimes []int, keysPressed string) byte {
    ans, m := keysPressed[0], releaseTimes[0]
    for i := 1; i < len(releaseTimes); i++{
        if diff := releaseTimes[i] - releaseTimes[i-1]; diff > m{
            ans, m = keysPressed[i], diff
        } else if diff == m && keysPressed[i] > ans {
            ans = keysPressed[i]
        }
    }
    return ans
}
```

```Python3
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        return max([(releaseTimes[0], keysPressed[0])] + [(releaseTimes[i] - releaseTimes[i-1], keysPressed[i]) for i in range(1, len(releaseTimes))])[1]
```