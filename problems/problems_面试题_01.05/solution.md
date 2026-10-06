# [Python/Java/JavaScript/Go] A simple edit-distance check with two pointers

> slug: pythonjavajavascriptgo-shuang-zhi-zhen-s-vojx
> date: 2022-05-12
> tags: Go, Java, JavaScript, Python, Python3
> question: One Away LCCI (one-away-lcci)
> url: https://leetcode.cn/problems/one-away-lcci/solutions/czNrD8/pythonjavajavascriptgo-shuang-zhi-zhen-s-vojx/

---
### Approach
The edit distance between the two strings must be at most 1. There is no need to compare every pair of positions as in the general edit-distance problem; compare characters in order, since at most one mismatch is allowed.

### Code

```Python3 []
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs((m:=len(first)) - (n:=len(second))) > 1:
            return False
        
        used, i, j = False, 0, 0
        while i < m and j < n:
            if first[i] == second[j]:
                i += 1
                j += 1
            elif used:
                return False
            else:
                # Use the lengths to distinguish three types of edit:
                if m > n:
                    # first is longer: delete its character at i and advance i
                    i += 1
                elif m < n:
                    # second is longer: delete its character at j and advance j
                    j += 1
                else:
                    # Edit the characters at i and j to match, then advance both
                    i += 1
                    j += 1
                used = True
        return True
```
```Java []
class Solution {
    public boolean oneEditAway(String first, String second) {
        int m = first.length(), n = second.length();
        if(Math.abs(m - n) > 1) {
            return false;
        }
        boolean used = false;
        for(int i = 0, j = 0; i < m && j < n; ) {
            if (first.charAt(i) == second.charAt(j)) {
                i++;
                j++;
            } else if (used) {
                return false;
            } else {
                if(m > n) {
                    i++;
                } else if(m < n) {
                    j++;
                } else {
                    i++;
                    j++;
                }
                used = true;
            }
        }
        return true;
    }
}
```
```JavaScript []
/**
 * @param {string} first
 * @param {string} second
 * @return {boolean}
 */
var oneEditAway = function(first, second) {
    const m = first.length, n = second.length
    if(Math.abs(m - n) > 1) {
        return false
    }
    for(let i = 0, j = 0, used = false; i < m && j < n; ) {
        if(first.charCodeAt(i) === second.charCodeAt(j)) {
            i++
            j++
        } else if (used) {
            return false
        } else {
            [i, j] = m > n ? [i + 1, j] : m < n ? [i, j + 1] : [i + 1, j + 1]
            used = true
        }
    }
    return true
};
```
```Go []
func oneEditAway(first string, second string) bool {
    m, n := len(first), len(second)
    if diff := m - n; diff < -1 || diff > 1 {
        return false
    }
    for i, j, used := 0, 0, false; i < m && j < n; {
        if first[i] == second[j] {
            i++
            j++
        } else if used {
            return false
        } else {
            if m > n {
                i++
            } else if m < n {
                j++
            } else {
                i++
                j++
            }
            used = true
        }
    }
    return true
}
```

A playful shortcut
```python3
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        return abs(diff:=len(first) - len(second)) <= 1 and (sum(a != b for a, b in zip(first, second)) <= 1 if diff == 0 else (any(first[:i] + first[i+1:] == second for i in range(len(first))) if diff == 1 else any(second[:i] + second[i+1:] == first for i in range(len(second)))))
```
