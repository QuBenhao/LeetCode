# [Python/Java] 模拟 and 优化

> slug: pythonjava-mo-ni-and-you-hua-by-himymben-was2
> date: 2021-09-12
> tags: Java, Python, Python3
> question: Valid Parenthesis String (valid-parenthesis-string)
> url: https://leetcode.cn/problems/valid-parenthesis-string/solutions/BXtlnC/pythonjava-mo-ni-and-you-hua-by-himymben-was2/

---
### 解题思路
纯模拟: 用一个集合记录所有当前可能的左括号个数，遇到左括号，所有可能数+1，遇到右括号，所有可能数-1，遇到星号，可能+1，可能不变，可能-1。左括号个数不能是负数，所以如果没有左括号个数的时候，可以返回False了。

**我们的集合里左括号个数的可能性其实是一个范围，从最低的一个数到最高的一个数全部都在，所以可以记录左右范围即可**。
因为就是在对一个范围进行偏移，左括号往右偏1，右括号往左偏1，星号往两边扩大1

### 代码

模拟
```Python3 []
class Solution:
    def checkValidString(self, s: str) -> bool:
        cur = {0}
        for c in s:
            nxt = set()
            if not cur:
                return False
            if c == '(':
                for val in cur:
                    nxt.add(val + 1)
            elif c == ')':
                for val in cur:
                    if val - 1 >= 0:
                        nxt.add(val - 1)
            else:
                for val in cur:
                    nxt.add(val + 1)
                    nxt.add(val)
                    if val - 1 >= 0:
                        nxt.add(val - 1)
            cur = nxt
        return 0 in cur
```
```Java []
class Solution {
    public boolean checkValidString(String s) {
        Set<Integer> cur = new HashSet<>();
        cur.add(0);
        for(int j=0;j<s.length();j++){
            if(cur.size() == 0)
                return false;
            char c = s.charAt(j);
            Set<Integer> nxt = new HashSet<>();
            if (c == '('){
                for(int i: cur)
                    nxt.add(i+1);
            }
            else if (c == ')'){
                for(int i: cur)
                    if (i - 1 >= 0)
                        nxt.add(i-1);
            }
            else{
                for(int i: cur){
                    nxt.add(i+1);
                    nxt.add(i);
                    if(i-1>=0)
                        nxt.add(i-1);
                }
            }
            cur = nxt;
        }
        return cur.contains(0);
    }
}
```

优化
```Python3 []
class Solution:
    def checkValidString(self, s: str) -> bool:
        # l表示当前左括号最少可能为多少，r表示当前左括号最多可能是多少，他们之间都可以取到
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
                r += 1
            elif c == ')':
                l -= 1
                r -= 1
            else:
                l -= 1
                r += 1
            if l < 0:
                l += 1
            if r < 0:
                return False
        return l == 0

```
```Java []
class Solution {
    public boolean checkValidString(String s) {
        int l = 0;
        for(int i = 0, r = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c == '('){
                l++;
                r++;
            } else if (c == ')'){
                if(r == 0)
                    return false;
                l--;
                r--;
            } else{
                l--;
                r++;
            }
            if(l < 0)
                l++;
        }
        return l == 0;
    }
}
```