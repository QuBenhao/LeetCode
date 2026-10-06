# [Python/Java/JavaScript/Go] Simulation

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-utd5
> date: 2022-04-06
> tags: Go, Java, JavaScript, Python, Python3
> question: Rotate String (rotate-string)
> url: https://leetcode.cn/problems/rotate-string/solutions/MJeavV/pythonjavajavascriptgo-mo-ni-by-himymben-utd5/

---
### Approach
A rotation starts at any position and continues until it wraps back to that position.
It is therefore a substring of two concatenated copies of the original string

PS:
Doubling the array is a common trick in problems where the end connects to the beginning

### Code

```Python3 []
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s
```
```Java []
class Solution {
    public boolean rotateString(String s, String goal) {
        return s.length() == goal.length() && (s + s).contains(goal);
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function(s, goal) {
    return s.length == goal.length && (s + s).indexOf(goal) != -1
};
```
```Go []
func rotateString(s string, goal string) bool {
    return len(s) == len(goal) && strings.Contains(s + s, goal)
}
```
