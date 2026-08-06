# [Python/Java/JavaScript/Go] 双指针实现简单编辑距离

> slug: pythonjavajavascriptgo-shuang-zhi-zhen-s-vojx
> date: 2022-05-12
> tags: Go, Java, JavaScript, Python, Python3
> question: One Away LCCI (one-away-lcci)
> url: https://leetcode.cn/problems/one-away-lcci/solutions/czNrD8/pythonjavajavascriptgo-shuang-zhi-zhen-s-vojx/

---
### 解题思路
本题要求两个字符串的编辑距离不超过1，我们不需要像编辑距离一样统计对比所有位置了，只需要依次比较不同，因为最多有一处。

### 代码

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
                # 根据长度判断三种变化:
                if m > n:
                    # first长，删掉i，i后移
                    i += 1
                elif m < n:
                    # second长，删掉j，j后移
                    j += 1
                else:
                    # 编辑i与j一致，一起后移
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

皮一下
```python3
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        return abs(diff:=len(first) - len(second)) <= 1 and (sum(a != b for a, b in zip(first, second)) <= 1 if diff == 0 else (any(first[:i] + first[i+1:] == second for i in range(len(first))) if diff == 1 else any(second[:i] + second[i+1:] == first for i in range(len(second)))))
```