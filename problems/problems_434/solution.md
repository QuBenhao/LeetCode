# [Python/Java/JavaScript] 模拟

> slug: pythonjavajavascript-mo-ni-by-himymben-1pex
> date: 2021-10-06
> tags: Java, JavaScript, Python, Python3
> question: Number of Segments in a String (number-of-segments-in-a-string)
> url: https://leetcode.cn/problems/number-of-segments-in-a-string/solutions/CpCU6Q/pythonjavajavascript-mo-ni-by-himymben-1pex/

---
### 解题思路
遍历统计个数即可

### 代码

```Python3 []
class Solution:
    def countSegments(self, s: str) -> int:
        return sum(st != "" for st in s.split(" "))
```
```Java []
class Solution {
    public int countSegments(String s) {
        int n = s.length(), ans = 0;
        char last = ' ';
        for(int i=0;i<n;i++){
            char c = s.charAt(i);
            if(c == ' ' && last != ' ')
                ans++;
            last = c;
        }
        return last != ' '? ans+1 : ans;
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @return {number}
 */
var countSegments = function(s) {
    let ans = 0, last = " ";
    for(let c of s){
        if(c == " " && last != " ")
            ans++;
        last = c;
    }
    return last == " " ? ans : ans + 1;
};
```