# [Python/Java/JavaScript/Go] 要么相同且有重复的字母可以交换，要么只有两个不同交换就一致

> slug: pythonjavajavascriptgo-yao-yao-xiang-ton-5ylz
> date: 2021-11-22
> tags: Go, Java, JavaScript, Python, Python3
> question: Buddy Strings (buddy-strings)
> url: https://leetcode.cn/problems/buddy-strings/solutions/ZvMEPG/pythonjavajavascriptgo-yao-yao-xiang-ton-5ylz/

---
### 解题思路
根据题意，必须交换一次，交换一次后一致的情况只有两种：
1. 本身字符串是一致的，有相同的字母，交换相同的字母仍然一致
2. 本身字符串刚好有两个字母顺序对调了，交换后正好一致

### 代码

```python3 []
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        x, y, cnts = -1, -1, [0] * 26
        for i in range(len(s)):
            cnts[ord(s[i]) - ord('a')] += 1
            if s[i] != goal[i]:
                if x == -1:
                    x = i
                elif y == -1:
                    y = i
                # 有三个不同了
                else:
                    return False
        # 必须是两种情况
        return (x != -1 and y != -1 and s[x] == goal[y] and goal[x] == s[y] ) or (x == -1 and y == -1 and any(c > 1 for c in cnts))
```
```Java []
class Solution {
    public boolean buddyStrings(String s, String goal) {
        if(s.length() != goal.length())
            return false;
        int x = -1, y = -1;
        int[] cnts = new int[26];
        for(int i=0;i<s.length();i++){
            cnts[s.charAt(i) - 'a']++;
            if(s.charAt(i) != goal.charAt(i))
                if(x == -1)
                    x = i;
                else if(y == -1)
                    y = i;
                else
                    return false;
        }
        if(x == -1 && y == -1){
            for(int i=0;i<26;i++){
                if(cnts[i] > 1)
                    return true;
            }
        }
        if(x != -1 && y != -1)
            if(s.charAt(x) == goal.charAt(y) && s.charAt(y) == goal.charAt(x))
                return true;
        return false;
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var buddyStrings = function(s, goal) {
    if(s.length != goal.length)
        return false;
    let x = -1, y = -1;
    const cnts = new Array(26);
    cnts.fill(0);
    for(let i=0;i<s.length;i++){
        cnts[s[i].charCodeAt() - 'a'.charCodeAt()]++;
        if(s[i] != goal[i]){
            if(x == -1)
                x = i;
            else if(y == -1)
                y = i;
            else
                return false;
        }
    }
    if(x == -1 && y == -1){
        for(let i=0;i<26;i++)
            if(cnts[i] > 1)
                return true;
    }
    if(x != -1 && y != -1)
        if(s[x] == goal[y] && s[y] == goal[x])
            return true;
    return false;
};
```
```Go []
func buddyStrings(s string, goal string) bool {
    if len(s) != len(goal){
        return false
    }
    x, y, cnts := -1, -1, [26]int{}
    for i := range s {
        cnts[s[i] - byte('a')]++
        if(s[i] != goal[i]){
            if(x == -1){
                x = i
            }else if(y == -1){
                y = i
            }else{
                return false
            }
        }
    }
    if(x == -1 && y == -1){
        for _, v := range cnts {
            if v > 1{
                return true
            }
        }
    }
    if(x != -1 && y != -1){
        if s[x] == goal[y] && s[y] == goal[x]{
            return true
        }
    }
    return false
}
```

差点儿忘了有人可能需要一行
```python3
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and ((not (d:=sum(s[i] != goal[i] for i in range(len(s)))) and len(set(s)) < len(s)) or (d == 2 and Counter(s) == Counter(goal)))
```