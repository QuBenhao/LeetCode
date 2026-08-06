# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-utd5
> date: 2022-04-06
> tags: Go, Java, JavaScript, Python, Python3
> question: Rotate String (rotate-string)
> url: https://leetcode.cn/problems/rotate-string/solutions/MJeavV/pythonjavajavascriptgo-mo-ni-by-himymben-utd5/

---
### 解题思路
所谓的旋转其实就是以任意位置开始，到转回来自己结束。
即为两个原字符串拼接的子串

PS:
在很多尾和头相连的数组题目中，都常使用两倍数组的小技巧

### 代码

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