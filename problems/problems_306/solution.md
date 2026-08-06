# [Python/Java/JavaScript/Go] 字符串加法 + 深度优先搜索

> slug: pythonjavajavascriptgo-zi-fu-chuan-jia-f-w5by
> date: 2022-01-09
> tags: Go, Java, JavaScript, Python, Python3
> question: Additive Number (additive-number)
> url: https://leetcode.cn/problems/additive-number/solutions/U4cBvb/pythonjavajavascriptgo-zi-fu-chuan-jia-f-w5by/

---
### 解题思路
字符串加法不会有精度的问题。
搜索的时候注意数字不能以0开头且有位数。

每次求出加和往后推判断是否满足即可。

### 代码

```Python3 []
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def helper(a, b):
            i, j, res, one = len(a) - 1, len(b) - 1, [], 0
            while i >= 0 or j >= 0:
                curA = curB = 0
                if i >= 0:
                    curA = int(a[i])
                    i -= 1
                if j >= 0:
                    curB = int(b[j])
                    j -= 1
                cur = curA + curB + one
                if cur >= 10:
                    cur %= 10
                    one = 1
                else:
                    one = 0
                res.append(str(cur))
            if one:
                res.append("1")
            return "".join(res[::-1])
        
        def dfs(p, q):
            last, first, second = 0, p, q
            while second < len(num):
                if (num[last] == '0' and first > last + 1) or (num[first] == '0' and second > first + 1):
                    return False
                s = helper(num[last:first], num[first:second])
                if num[second:second+len(s)] != s:
                    return False
                last, first, second = first, second, second + len(s)
            return True
        
        for i in range(1, len(num) - 1):
            for j in range(i + 1, len(num)):
                if dfs(i, j):
                    return True
        return False
```
```Java []
class Solution {
    public boolean isAdditiveNumber(String num) {
        for(int i=1;i<num.length()-1;i++)
            for(int j=i+1;j<num.length();j++)
                if(dfs(i, j, num))
                    return true;
        return false;
    }

    private String add(String a, String b){
        StringBuilder sb = new StringBuilder();
        int one = 0;
        for(int i=a.length()-1,j=b.length()-1;i>=0||j>=0;){
            int curA = 0, curB = 0;
            if(i >= 0)
                curA = a.charAt(i--) - '0';
            if(j >= 0)
                curB = b.charAt(j--) - '0';
            int cur = curA + curB + one;
            one = cur >= 10 ? 1 : 0;
            sb.append((char)('0' + cur%10));
        }
        if(one == 1)
            sb.append('1');
        return sb.reverse().toString();
    }

    private boolean dfs(int i, int j, String num){
        int last = 0, first = i, second = j;
        while(second < num.length()){
            if((num.charAt(last) == '0' && first > last + 1) || (num.charAt(first) == '0' && second > first + 1))
                return false;
            String s = add(num.substring(last, first), num.substring(first, second));
            if(second + s.length() > num.length() || !s.equals(num.substring(second, second + s.length())))
                return false;
            last = first;
            first = second;
            second += s.length();
        }
        return true;
    }
}
```
```JavaScript []
/**
 * @param {string} num
 * @return {boolean}
 */
var isAdditiveNumber = function(num) {
    add = function(a, b){
        const res = new Array()
        let one = 0
        for(let i=a.length-1,j=b.length-1;i>=0||j>=0;){
            let curA = 0, curB = 0
            if(i >= 0)
                curA = a.charCodeAt(i--) - '0'.charCodeAt(0)
            if(j >= 0)
                curB = b.charCodeAt(j--) - '0'.charCodeAt(0)
            const cur = curA + curB + one
            one = cur >= 10 ? 1 : 0
            res.push(String.fromCodePoint(cur % 10 + '0'.charCodeAt(0)))
        }
        if(one == 1)
            res.push('1')
        return res.reverse().join('')
    }

    dfs = function(i, j){
        let last = 0, first = i, second = j;
        while(second < num.length){
            if((num.charAt(last) == '0' && first > last + 1) || (num.charAt(first) == '0' && second > first + 1))
                return false
            const s = add(num.substring(last, first), num.substring(first, second));
            if(second + s.length > num.length || !(s === num.substring(second, second + s.length)))
                return false
            last = first
            first = second
            second += s.length
            console.log(last, first, second)
        }
        return true
    }

    for(let i=1;i<num.length-1;i++)
        for(let j=i+1;j<num.length;j++)
            if(dfs(i, j))
                return true
    return false
};
```
```Go []
func add(a, b string) string {
    res, one := []byte{}, 0
    for i, j := len(a) - 1, len(b) - 1 ; i >= 0 || j >= 0 ; {
        curA, curB := 0, 0
        if i >= 0 {
            curA = int(a[i] - '0')
            i--
        }
        if j >= 0 {
            curB = int(b[j] - '0')
            j--
        }
        cur := curA + curB + one
        one = cur/10
        res = append(res, byte(cur%10)+'0')
    }
    if one == 1 {
        res = append(res, '1')
    }
    for i, n := 0, len(res); i < n/2; i++ {
        res[i], res[n-1-i] = res[n-1-i], res[i]
    }
    return string(res)
}

func dfs(num string, first, second int) bool {
    n, last := len(num), 0
    for second < n {
        if (num[last] == '0' && first > last + 1) || (num[first] == '0' && second > first + 1){
            return false
        }
        s := add(num[last:first], num[first:second])
        if second + len(s) > n || num[second:second + len(s)] != s {
            return false
        }
        last, first, second = first, second, second + len(s)
    }
    return true
}

func isAdditiveNumber(num string) bool {
    for i:=1;i<len(num)-1;i++ {
        for j:=i+1;j<len(num);j++{
            if dfs(num, i, j){
                return true
            }
        }
    }
    return false
}
```
补充一个简洁版本
```python3
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1, len(num) - 1):
            for j in range(i + 1, len(num)):
                last, first, second = 0, i, j
                while second < len(num):
                    if (num[last] == '0' and first > last + 1) or (num[first] == '0' and second > first + 1) or len(num) - second < second - first:
                        break
                    s = str(int(num[last:first]) + int(num[first:second]))
                    if s != num[second:second+len(s)]:
                        break
                    last, first, second = first, second, second + len(s)
                else:
                    return True
        return False
```