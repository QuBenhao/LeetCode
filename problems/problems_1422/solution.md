# [Python3/Java/TypeScript/Go/Js/C++/C/C#/PHP/Python] Prefix sums and dynamic programming

> slug: -by-himymben-schd
> date: 2022-08-14
> tags: C, C++, C#, Go, Java, JavaScript, PHP, Python, Python3, TypeScript
> question: Maximum Score After Splitting a String (maximum-score-after-splitting-a-string)
> url: https://leetcode.cn/problems/maximum-score-after-splitting-a-string/solutions/I1w9Ed/-by-himymben-schd/

---
### Approach
This is exactly the same as [2155](https://leetcode.cn/problems/all-divisions-with-the-highest-score-of-a-binary-array/solution/pythongo-qian-zhui-he-by-himymben-2fnr/) (which explains why it felt familiar).

A natural approach uses prefix sums to count 0s on the left and 1s on the right, then tries every split.
A key condition is that the string contains only 0 and 1, so their counts complement each other: every additional 0 means one fewer 1, and the two counts always sum to the string length.
Let the total string length be $n$.
If the total number of 0s is $finalPresum$ and the number of 0s left of the current split is $presum$,
the number of 1s on the right is $(n - i) - (finalPresum - presum)$.
This is the right substring's length minus its number of 0s.
Separate the variable and constant terms to simplify the score at each position:
$presum + (n - i) - (finalPresum - presum) = presum * 2 - i + (n - finalPresum)$
We only need to find the $i$ that maximizes $presum * 2 - i$.

PS:
The split cannot be at either edge.

### Code

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

### Complexity

Time complexity: $o(n)$
Space complexity: $o(1)$
