# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-06-26
> Upvotes: 27
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
首先一个字符串的子序列如果不是其他字符串的子序列，那么这个字符串本身也一定不是。
因为包含这个字符串本身的，一定也能包含它的任意子序列。
所以题目变为从字符串数组中找最长的一个原字符串，该字符串不是其他字符串的子序列。
根据数据范围，暴力模拟判断即可。

### 代码

```Python3 []
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_sub_str(s1: str, s2: str) -> bool:
            if len(s2) < len(s1):
                return False
            i = j = 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == len(s1)
        
        ans = -1
        for i, s in enumerate(strs):
            if len(s) > ans and all(not is_sub_str(s, s_) for j, s_ in enumerate(strs) if j != i):
                ans = len(s)
        return ans
```
```Java []
class Solution {
    public int findLUSlength(String[] strs) {
        int ans = -1;
        out:
        for (int i = 0; i < strs.length; i++) {
            if (strs[i].length() > ans) {
                for (int j = 0; j < strs.length; j++) {
                    if (j != i && isSubStr(strs[i], strs[j])) {
                        continue out;
                    }
                }
                ans = strs[i].length();
            }
        }
        return ans;
    }

    private boolean isSubStr(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        if (m > n) {
            return false;
        }
        int i = 0;
        for (int j = 0; i < m && j < n; j++) {
            if (s1.charAt(i) == s2.charAt(j)) {
                i++;
            }
        }
        return i == m;
    }
}
```
```TypeScript []
function findLUSlength(strs: string[]): number {
    let ans = -1
    out:
    for (let [i, s] of strs.entries()) {
        if (s.length > ans) {
            for (let [j, s_] of strs.entries()) {
                if (j != i && isSubStr(s, s_)) {
                    continue out
                }
            }
            ans = s.length
        }
    }
    return ans
};

function isSubStr(s1: string, s2:string): boolean {
    const m = s1.length, n = s2.length
    if (m > n) {
        return false
    }
    let i = 0
    for (let j = 0; i < m && j < n; j++) {
        if (s1.charCodeAt(i) === s2.charCodeAt(j)) {
            i++
        }
    }
    return i == m
}
```
```Go []
func findLUSlength(strs []string) int {
    ans := -1
    out:
    for i, s := range strs {
        if len(s) > ans {
            for j, s_ := range strs {
                if j != i && isSubStr(s, s_) {
                    continue out
                }
            }
            ans = len(s)
        }
    }
    return ans
}

func isSubStr(s1, s2 string) bool {
    m, n := len(s1), len(s2)
    if m > n {
        return false
    }
    i := 0
    for j := 0; i < m && j < n; j++ {
        if s1[i] == s2[j] {
            i++
        }
    }
    return i == m
}
```