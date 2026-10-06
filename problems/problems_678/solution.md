# [Python/Java] Simulation and optimization

> slug: pythonjava-mo-ni-and-you-hua-by-himymben-was2
> date: 2021-09-12
> tags: Java, Python, Python3
> question: Valid Parenthesis String (valid-parenthesis-string)
> url: https://leetcode.cn/problems/valid-parenthesis-string/solutions/BXtlnC/pythonjava-mo-ni-and-you-hua-by-himymben-was2/

---
### Approach
Direct simulation: keep a set of all possible counts of unmatched left parentheses. A left parenthesis adds 1 to each count; a right parenthesis subtracts 1; an asterisk may add 1, leave the count unchanged, or subtract 1. Counts cannot be negative. If no valid count remains, return False.

**The possible counts form a continuous range from the minimum to the maximum, so we only need its two endpoints.**
Each step shifts or expands this range: a left parenthesis shifts it right by 1, a right parenthesis shifts it left by 1, and an asterisk expands it by 1 in both directions.

### Code

Simulation
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

Optimization
```Python3 []
class Solution:
    def checkValidString(self, s: str) -> bool:
        # l and r are the minimum and maximum possible unmatched-left-parenthesis counts; every value between them is possible
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
