# [Python3/Java/TypeScript/Go/Js/C++/C/C#/PHP/Python] 前缀和动态规划

> slug: -by-himymben-schd
> date: 2022-08-14
> tags: C, C++, C#, Go, Java, JavaScript, PHP, Python, Python3, TypeScript
> question: Maximum Score After Splitting a String (maximum-score-after-splitting-a-string)
> url: https://leetcode.cn/problems/maximum-score-after-splitting-a-string/solutions/I1w9Ed/-by-himymben-schd/

---
### 解题思路
本题和[2155](https://leetcode.cn/problems/all-divisions-with-the-highest-score-of-a-binary-array/solution/pythongo-qian-zhui-he-by-himymben-2fnr/)一模一样（我说我怎么感觉做过）。

很容易想到利用前缀和，分别统计左边0和右边1，然后枚举答案。
但是本题有一个很大的条件是字符串只有0和1，那么0和1的个数就是对称的，有多少个0就少多少个1，两者加起来永远是字符串长度。
那么设字符串总长度为$n$，
假如我们知道总共0的个数$finalPresum$和当前分割位置左侧0的个数$presum$,
可以计算出右侧1的个数为$(n - i) - (finalPresum - presum)$
这个式子的含义是右边字符串长度减去右边0的个数。
将变量和常量分别抽出来，于是每个位置的得分可以化简为:
$presum + (n - i) - (finalPresum - presum) = presum * 2 - i + (n - finalPresum)$
我们只需要找到$i$, 使得$presum * 2 - i$最大即可。

PS:
注意不可割在边缘

### 代码

```Python3 []
class Solution:
    def maxScore(self, s: str) -> int:
        n, presum, ans = len(s), 0, -inf
        for i in range(n):
            # cur = presum + (n - i - final_presum + presum) = presum * 2 - i + (n - final_presum)
            if i and (cur := presum * 2 - i) > ans:
                ans = cur
            presum += s[i] == "0"
        return ans + n - presum
```
```Python []
class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, presum, ans = len(s), 0, -1 - len(s)
        for i in xrange(n):
            if i and presum * 2 - i > ans:
                ans = presum * 2 - i
            presum += s[i] == "0"
        return ans + n - presum
```
```Java []
class Solution {
    public int maxScore(String s) {
        int n = s.length(), presum = 0, ans = -1 - s.length();
        for (int i = 0; i < n; i++) {
            if (i > 0 && presum * 2 - i > ans) {
                ans = presum * 2 - i;
            }
            presum += s.charAt(i) == '0' ? 1 : 0;
        }
        return ans + n - presum;
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @return {number}
 */
var maxScore = function(s) {
    const n = s.length
    let presum = 0, ans = -1 - n
    for (let i = 0; i < n; i++) {
        if (i > 0 && presum * 2 - i > ans) {
            ans = presum * 2 - i
        }
        presum += s.charAt(i) === '0' ? 1 : 0
    }
    return ans + n - presum
};
```
```TypeScript []
function maxScore(s: string): number {
    const n: number = s.length
    let presum: number = 0, ans: number = -1 - n
    for (let i = 0; i < n; i++) {
        if (i > 0 && presum * 2 - i > ans) {
            ans = presum * 2 - i
        }
        presum += s.charAt(i) === '0' ? 1 : 0
    }
    return ans + n - presum
};
```
```Go []
func maxScore(s string) int {
    n := len(s)
    presum, ans := 0, -1 - n
    for i := 0; i < n; i++ {
        if cur := presum * 2 - i; i > 0 && cur > ans {
            ans = cur
        }
        if s[i] == '0' {
            presum++
        }
    }
    return ans + n - presum
}
```
```C++ []
class Solution {
public:
    int maxScore(string s) {
        int n = s.size();
        int presum = 0, ans = -1 - n;
        for (int i = 0; i < n; i++) {
            if (i > 0 && presum * 2 - i > ans) {
                ans = presum * 2 - i;
            }
            presum += s[i] == '0' ? 1 : 0;
        }
        return ans + n - presum;
    }
};
```
```C []
int maxScore(char * s){
    int n = strlen(s);
    int presum = 0, ans = -1 - n;
    for (int i = 0; i < n; i++) {
        if (i > 0 && presum * 2 - i > ans) {
            ans = presum * 2 - i;
        }
        if (s[i] == '0') {
            presum++;
        }
    }
    return ans + n - presum;
}
```
```C# []
public class Solution {
    public int MaxScore(string s) {
        int n = s.Length;
        int presum = 0, ans = -1 - n;
        for (int i = 0; i < n; i++) {
            if (i > 0 && presum * 2 - i > ans) {
                ans = presum * 2 - i;
            }
            if (s[i] == '0') {
                presum++;
            }
        }
        return ans + n - presum;
    }
}
```
```Php []
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxScore($s) {
        $n = strlen($s);
        $presum = 0;
        $ans = -1 - $n;
        for ($i = 0; $i < $n; $i++) {
            if ($i > 0 && $presum * 2 - $i > $ans) {
                $ans = $presum * 2 - $i;
            }
            if ($s[$i] == '0') {
                $presum++;
            }
        }
        return $ans + $n - $presum;
    }
}
```

### 复杂度

时间复杂度 $o(n)$
空间复杂度 $o(1)$