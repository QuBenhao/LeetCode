# [Python/Java/JavaScript/Go] 模拟

> slug: pythonjavajavascriptgo-mo-ni-by-himymben-7w0h
> date: 2022-05-03
> tags: Go, Java, JavaScript, Python, Python3
> question: Reorder Data in Log Files (reorder-data-in-log-files)
> url: https://leetcode.cn/problems/reorder-data-in-log-files/solutions/yi9qv5/pythonjavajavascriptgo-mo-ni-by-himymben-7w0h/

---
### 解题思路
按题目要求自定义lambda排序比较器

特别说明:
Python sort和sorted是稳定的。
Java Arrays.sort 在比较对象时是稳定的，在比较int等基本类型使用了快排是不稳定的。Collections.sort 是稳定的。

### 代码

```Python3 []
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=lambda log: (0, log.split(' ')[1:], log.split(' ')[0]) if log[-1].isalpha() else (1,))
```
```Java []
class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Arrays.sort(logs, (a, b) -> {
            char aLast = a.charAt(a.length() - 1), bLast = b.charAt(b.length() - 1);
            boolean aDig = aLast >= '0' && aLast <= '9', bDig = bLast >= '0' && bLast <= '9';
            if(aDig && bDig)
                return 0;
            else if(aDig)
                return 1;
            else if(bDig)
                return -1;
            String[] aSp = a.split(" ", 2), bSp = b.split(" ", 2);
            int cmp = aSp[1].compareTo(bSp[1]);
            if(cmp != 0)
                return cmp;
            return aSp[0].compareTo(bSp[0]);
        });
        return logs;
    }
}
```
```JavaScript []
/**
 * @param {string[]} logs
 * @return {string[]}
 */
const ZERO = '0'.charCodeAt(0), NINE = '9'.charCodeAt(0)
var reorderLogFiles = function(logs) {
    logs.sort((a,b)=>{
        const aDig = a.charCodeAt(a.length - 1) >= ZERO && a.charCodeAt(a.length - 1) <= NINE,
              bDig = b.charCodeAt(b.length - 1) >= ZERO && b.charCodeAt(b.length - 1) <= NINE
        if(aDig && bDig)
            return 0
        else if(aDig)
            return 1
        else if(bDig)
            return -1
        const aSp = a.split(" "), bSp = b.split(" ")
        const cmp = aSp.slice(1).join(" ").localeCompare(bSp.slice(1).join(" "))
        if(cmp != 0)
            return cmp
        return aSp[0].localeCompare(bSp[0])
    })
    return logs
};
```
```Go []
func reorderLogFiles(logs []string) []string {
    sort.SliceStable(logs, func(i, j int) bool {
        a, b := logs[i], logs[j]
        aDig := unicode.IsDigit(rune(a[len(a) - 1]))
        bDig := unicode.IsDigit(rune(b[len(b) - 1]))
        if (aDig && bDig) {
            return i < j
        } else if bDig {
            return true
        } else if aDig {
            return false
        }
        aSp := strings.SplitN(a, " ", 2)
        bSp := strings.SplitN(b, " ", 2)
        if aSp[1] == bSp[1] {
            return aSp[0] < bSp[0]
        }
        return aSp[1] < bSp[1]
    })
    return logs
}
```