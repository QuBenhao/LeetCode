# [Python/Java/JavaScript/Go] 双指针 or 动态规划

> Author: Benhao
> Date: 2022-04-18
> Upvotes: 32
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
双指针：
我们可以在遍历的时候记录上一次遇到c的位置，每次先更新距离为到上次遇到c的距离，直到遇到了另一个c。
我们将这个c和上一个c的中点，到这个c之间的点，更新为更近的新的c到距离即可。同时上一个c变成了这个c。


动态规划：
在类似接雨水的题目中，我们使用简单的正反遍历动态规划。
正反遍历可能更好理解一些，虽然时间会更久一点儿，但复杂度一样。
从左往右看，我们可以知道所有点到它左边的c的距离；
从右往左看，我们可以知道所有点到它右边的c的距离；
每个点的答案为两个距离的更小值。

### 代码

双指针
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

正反遍历
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
            # 因为两者都有 len(s) - 1 的偏移量，可以一起去掉，减少运算            
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