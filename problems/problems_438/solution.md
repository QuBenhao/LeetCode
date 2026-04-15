# [Python/Java/JavaScript/Go] 滑动窗口 -> 定长优化 -> 常数优化

> Author: Benhao
> Date: 2021-11-27
> Upvotes: 20
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
我们不在乎顺序，只在乎字母的个数，可以使用滑动窗口，维护窗口内各个字母的个数，当窗口中各字母个数和p的一致时，窗口的头就是想要的答案了。

既然要求长度是一致的，那么我们显然始终要比的也是一样长度的字符串，也就是和p一样长的固定窗口，这时候只需要用一个指针就可以完成滑动了。

每次比较26位的区别是没有必要的，因为变动总是一个字母，一位的变动，可以维护一个当前窗口和p的统计的不一样的个数，维护在同一个哈希表里，
当某位变成零，不一样的个数减一；当某位从零变成非零，不一样的个数加一。只有当不一样的个数为0时，才是想要的答案。

### 代码

```Python3
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnts_p = [0] * 26
        for c in p:
            cnts_p[ord(c) - ord('a')] += 1
        window, cur = deque([]), [0] * 26
        ans = []
        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            cur[idx] += 1
            if cur == cnts_p:
                ans.append(i - len(p) + 1)
            window.append(c)
            if window and (len(window) == len(p) or cur[idx] > cnts_p[idx]):
                l = window.popleft()
                cur[ord(l) - ord('a')] -= 1
        return ans
```
```Python3 []
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        ans = []
        if m < n:
            return ans
        cnts_p = [0] * 26
        for c in p:
            cnts_p[ord(c) - ord('a')] += 1
        cur = [0] * 26
        for i in range(m):
            cur[ord(s[i]) - ord('a')] += 1
            if i >= n - 1:
                if cur == cnts_p:
                    ans.append(i - n + 1)
                cur[ord(s[i - n + 1]) - ord('a')] -= 1
        return ans
```
```Java []
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int m = s.length(), n = p.length();
        List<Integer> ans = new ArrayList<>();
        if(m < n)
            return ans;
        int[] cntsP = new int[26], cnts = new int[26];
        for(int i=0;i<n;i++)
            cntsP[p.charAt(i)-'a']++;
        for(int i=0;i<m;i++){
            cnts[s.charAt(i)-'a']++;
            if(i>=n-1){
                if(Arrays.equals(cnts,cntsP))
                    ans.add(i-n+1);
                cnts[s.charAt(i-n+1)-'a']--;
            }
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    function arrayEqual(a, b){
        for(let i=0;i<a.length;i++)
            if(a[i] !== b[i])
                return false
        return true
    }

    const m = s.length, n = p.length
    ans = []
    if(m < n)
        return ans
    const cntsP = new Array(26), cnts = new Array(26)
    cntsP.fill(0)
    cnts.fill(0)
    for(let i=0;i<n;i++)
        cntsP[p.charCodeAt(i) - 'a'.charCodeAt()]++
    for(let i=0;i<=m;i++){
        cnts[s.charCodeAt(i)-'a'.charCodeAt()]++
        if(i>=n-1){
            if(arrayEqual(cntsP, cnts))
                ans.push(i-n+1)
            cnts[s.charCodeAt(i-n+1)-'a'.charCodeAt()]--
        }
    }
    return ans
};
```
```Go []
func findAnagrams(s string, p string) (ans []int) {
    m, n := len(s), len(p)
    if m < n {
        return ans
    }
    var cntsP, cnts [26]int
    for i := 0; i < n; i++ {
        cntsP[p[i] - byte('a')]++
    }
    for i := 0; i < m; i++ {
        cnts[s[i] - byte('a')]++
        if i >= n - 1 {
            if cnts == cntsP {
                ans = append(ans, i - n + 1)
            }
            cnts[s[i-n+1] - byte('a')]--
        }
    }
    return ans
}
```
---
```Python3 []
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def maintain(key, val):
            before = cnts[key] == 0
            cnts[key] += val
            if before:
                return 1
            elif not cnts[key]:
                return -1
            return 0

        m, n = len(s), len(p)
        ans = []
        if m < n:
            return ans
        cnts = [0] * 26
        for c in p:
            cnts[ord(c) - ord('a')] -= 1
        diff = sum(cnt != 0 for cnt in cnts)
        for i in range(m):
            diff += maintain(ord(s[i]) - ord('a'), 1)
            if i >= n - 1:
                if not diff:
                    ans.append(i - n + 1)
                diff += maintain(ord(s[i - n + 1]) - ord('a'), -1)
        return ans
```
```Java []
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int m = s.length(), n = p.length();
        List<Integer> ans = new ArrayList<>();
        if(m < n)
            return ans;
        int[] cnts = new int[26];
        for(int i=0;i<n;i++)
            cnts[p.charAt(i)-'a']--;
        int diff = 0;
        for(int i=0;i<cnts.length;i++)
            if(cnts[i]!=0)
                diff++;
        for(int i=0;i<m;i++){
            diff += maintain(cnts,s.charAt(i)-'a',1);
            if(i>=n-1){
                if(diff == 0)
                    ans.add(i-n+1);
                diff += maintain(cnts,s.charAt(i-n+1)-'a',-1);            
            }
        }
        return ans;
    }

    private int maintain(int[] cnts, int key, int val) {
        boolean old = cnts[key] == 0;
        cnts[key] += val;
        if(old){
            return 1;
        } else if(cnts[key] == 0){
            return -1;
        }
        return 0;
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    function maintain(cnts, key, val){
        const b = cnts[key] == 0
        cnts[key] += val
        if(b){
            return 1
        } else if(cnts[key] == 0){
            return -1
        }
        return 0
    }

    const m = s.length, n = p.length
    ans = []
    if(m < n)
        return ans
    const cnts = new Array(26)
    cnts.fill(0)
    for(let i=0;i<n;i++)
        cnts[p.charCodeAt(i) - 'a'.charCodeAt()]--
    let diff = 0
    for(let i=0;i<cnts.length;i++)
        if(cnts[i] != 0)
            diff++
    for(let i=0;i<=m;i++){
        diff += maintain(cnts,s.charCodeAt(i)-'a'.charCodeAt(), 1)
        if(i>=n-1){
            if(diff == 0)
                ans.push(i-n+1)
            diff += maintain(cnts,s.charCodeAt(i-n+1)-'a'.charCodeAt(), -1)
        }
    }
    return ans
};
```
```Go []
func findAnagrams(s string, p string) (ans []int) {
    maintain := func(cnts *[26]int, key byte, val int) int {
        b := cnts[key] == 0
        cnts[key] += val
        if b {
            return 1
        } else if(cnts[key] == 0) {
            return -1
        }
        return 0
    }

    m, n := len(s), len(p)
    if m < n {
        return ans
    }
    var cnts [26]int
    for i := 0; i < n; i++ {
        cnts[p[i] - byte('a')]--
    }
    diff := 0
    for i := 0; i < len(cnts); i++ {
        if cnts[i] != 0 {
            diff++
        }
    }
    for i := 0; i < m; i++ {
        diff += maintain(&cnts,s[i] - byte('a'),1)
        if i >= n - 1 {
            if diff == 0 {
                ans = append(ans, i - n + 1)
            }
            diff += maintain(&cnts, s[i-n+1] - byte('a'), -1)
        }
    }
    return ans
}
```