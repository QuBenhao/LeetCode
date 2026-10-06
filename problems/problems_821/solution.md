# [Python/Java/JavaScript/Go] Two pointers or dynamic programming

> Author: Benhao
> Date: 2022-04-18
> Upvotes: 32
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
Two pointers:
While scanning, track the last position of c. Initially set each distance to the distance from that c until another c is encountered.
For positions between this c and the midpoint to the previous c, update the distance to this closer c. Then make this c the previous c.


Dynamic programming:
As in problems such as trapping rain water, use simple forward and backward passes for dynamic programming.
Forward and backward passes may be easier to understand. They take a little longer but have the same complexity.
A left-to-right pass gives every position's distance to the c on its left;
A right-to-left pass gives every position's distance to the c on its right;
The answer at each position is the smaller of these two distances.

### Code

Two pointers
```Python3 []
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans, last = [inf] * len(s), None
        for i, ch in enumerate(s):
            if ch == c:
                if last is not None:
                    for j in range(i, (i - 1 + last) // 2 - 1, -1):
                        ans[j] = min(ans[j], i - j)
                else:
                    for j in range(i, -1, -1):
                        ans[j] = min(ans[j], i - j)
                last = i
            elif last is not None:
                ans[i] = min(ans[i], i - last)
        return ans
```
```Java []
class Solution {
    public int[] shortestToChar(String s, char c) {
        int n = s.length();
        int[] ans = new int[n];
        Arrays.fill(ans, n);
        int last = -n;
        for(int i = 0; i < n; i++) {
            if(s.charAt(i) == c) {
                for(int j = i; j >= Math.max(0, (i + last - 1) / 2); j--)
                    ans[j] = Math.min(ans[j], i - j);
                last = i;
            } else
                ans[i] = Math.min(ans[i], i - last);
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @param {character} c
 * @return {number[]}
 */
var shortestToChar = function(s, c) {
    const n = s.length
    const ans = new Array(n).fill(n)
    for(let i = 0, last = -n; i < n; i++) {
        if(s.charCodeAt(i) == c.charCodeAt(0)) {
            for(let j = i; j >= Math.max(0, (last + i - 1) >> 1); j--)
                ans[j] = Math.min(ans[j], i - j)
            last = i
        } else
            ans[i] = Math.min(ans[i], i - last)
    }
    return ans
};
```
```Go []
func shortestToChar(s string, c byte) []int {
    n := len(s)
    ans := make([]int, n)
    for i, last := 0, -n; i < n; i++ {
        if s[i] == c {
            if last == -n {
                for j := i; j >= 0; j-- {
                    ans[j] = i - j
                }
            } else {
                for j := i; j > (i + last - 1) >> 1; j-- {
                    ans[j] = i - j
                }
            }
            last = i
        } else {
            ans[i] = i - last
        }
    }
    return ans
}
```

Forward and backward passes
```Python3 []
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans, last = [inf] * len(s), -inf
        for i, ch in enumerate(s):
            if ch == c:
                last = i
            ans[i] = min(ans[i], i - last)
        last = inf
        for i, ch in enumerate(s[::-1]):
            # Both have a len(s) - 1 offset, so cancel it from both to reduce computation            
            # if ch == c:
            #     last = len(s) - 1 - i
            # ans[-1 - i] = min(ans[-1 - i], last - len(s) + 1 + i)
            if ch == c:
                last = -i
            ans[-1 - i] = min(ans[-1 - i], last + i)
        return ans
```
```Java []
class Solution {
    public int[] shortestToChar(String s, char c) {
        int n = s.length();
        int[] ans = new int[n];
        Arrays.fill(ans, n);
        for(int i = 0, last = -n; i < n; i++) {
            if(s.charAt(i) == c)
                last = i;
            ans[i] = Math.min(ans[i], i - last);
        }
        for(int i = n - 1, last = n * 2; i >= 0; i--) {
            if(s.charAt(i) == c)
                last = i;
            ans[i] = Math.min(ans[i], last - i);
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @param {character} c
 * @return {number[]}
 */
var shortestToChar = function(s, c) {
    const n = s.length
    const ans = new Array(n).fill(n)
    for(let i = 0, last = -n; i < n; i++) {
        if(s.charCodeAt(i) == c.charCodeAt(0))
            last = i
        ans[i] = Math.min(ans[i], i - last)
    }
    for(let i = n - 1, last = 2 * n; i >= 0; i--) {
        if(s.charCodeAt(i) == c.charCodeAt(0))
            last = i
        ans[i] = Math.min(ans[i], last - i)
    }
    return ans
};
```
```Go []
func shortestToChar(s string, c byte) []int {
    n := len(s)
    ans := make([]int, n)
    for i, last := 0, -n; i < n; i++ {
        ans[i] = n
        if s[i] == c {
            ans[i] = 0
            last = i
        } else {
            ans[i] = i - last
        }
    }
    for i, last := n - 1, 2 * n; i >= 0; i-- {
        if s[i] == c {
            last = i
        } else if v := last - i; v < ans[i] {
            ans[i] = v
        }
    }
    return ans
}
```
